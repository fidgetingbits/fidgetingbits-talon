import json
import re


def file_extensions(x):
    x = re.sub("\\.py$", " dot pie", x)
    x = re.sub("\\.c$", " dot see", x)
    x = re.sub("\\.h$", " dot h", x)
    x = re.sub("\\.sh$", " dot s h", x)
    x = re.sub("\\.zsh$", " dot z s h", x)
    x = re.sub("\\.go$", " dot go", x)
    return x


def numbers(x):
    x = x.replace("0", " zero ")
    x = x.replace("1", " one ")
    x = x.replace("2", " two ")
    x = x.replace("3", " three ")
    x = x.replace("4", " four ")
    x = x.replace("5", " five ")
    x = x.replace("6", " six ")
    x = x.replace("7", " seven ")
    x = x.replace("8", " eight ")
    x = x.replace("9", " nine ")
    return x


def punctuation(x, specials):
    specials = specials or ""
    x = re.sub("\\.", " dot " if "." in specials else " ", x)
    x = re.sub("_", " under " if "_" in specials else " ", x)
    x = re.sub("-", " dash " if "-" in specials else " ", x)
    x = re.sub("/", " slash " if "/" in specials else " ", x)
    # talon pukes on multiple spaces
    x = re.sub(" +", " ", x)
    # talon also pukes on leading spaces
    return x.strip()


FULL = 1
NOPREFIX = 2
SHORTHAND = 3
SHORTHAND_NOPREFIX = 4


class Edit:
    """A compound type sometimes returned by a Speakifier talon list."""

    def __init__(self, prefix, results):
        self.prefix = prefix
        self.results = results


class Speakifier:
    """
    Speakifier calculates possible pronunciations from a set of symbols.  The
    general rule is that a symbol should be pronouncable by speaking just the
    plain words in a symbol, or by speaking them with explicit punctuation.

    Examples:
        big_long/file-name -> big long file name,
                              big under long slash file dash name
        dos2unix -> dos two unix
        c99 -> c nine nine

    Each symbol added to the speakifier is assumed to be unique, though its
    pronuncataion may not be unique.

    Examples, with prefix="my_dir/":
        my_dir/some-file -> some file
                            some dash file
        my_dir/other-file -> other file
                             other dash file

    If the prefix contains just text, allowable pronunciations include the
    symbol with and without the prefix.

    Examples, with prefix="my":
        my_variable -> my variable        # plain words of "my_variable"
                       my under variable  # explicit form of "my_variable"
                       variable           # plain form of "_variable"
                       under variable     # plain form of "variable"

    Finally, similar to tab-completion, speaking the first word of a multi-word
    symbol is allowed.

    Examples:
        big_long/file-name -> big
        dos2unix -> dos
        c99 -> c
    """

    def __init__(self, prefix=""):
        self.prefix = prefix

        # If there is a symbol in the prefix, we never allow pronouncing before
        # it.  Think of pronouncing "--amend" when "--" is the prefix or "a/b"
        # when "a/" is the prefix.  You wouldn't.
        symboled_prefix = re.match("(.*[0-9._/-])[^0-9._/-]*$", prefix)
        if symboled_prefix:
            self.dont_speak = len(symboled_prefix[1])
        else:
            self.dont_speak = 0

        # pronounce maps pronunciations into lists of matching typable symbols.
        self.pronounce = {}
        self.edits = {}

    def _add_pronunciation(self, speakable, symbol, kind):
        kinds = self.pronounce.setdefault(speakable, {})
        kinds[symbol] = min(kinds.get(symbol, kind), kind)

    def _gen_variations(self, speakable, symbol, kind):
        if not speakable:
            return

        # always start with pronouncing file extensions
        speakable = file_extensions(speakable)

        # always separate numbers into individual digits
        speakable = numbers(speakable)

        # then try to support the plainest form
        self._add_pronunciation(punctuation(speakable, None), symbol, kind)

        # support the most explicit form
        self._add_pronunciation(punctuation(speakable, "._-/"), symbol, kind)

        # support the one-of-each forms
        self._add_pronunciation(punctuation(speakable, "."), symbol, kind)
        self._add_pronunciation(punctuation(speakable, "_"), symbol, kind)
        self._add_pronunciation(punctuation(speakable, "-"), symbol, kind)
        self._add_pronunciation(punctuation(speakable, "/"), symbol, kind)

    def add_symbol(self, symbol):
        """Register a unique symbol with the speakifier"""
        speakable = symbol[self.dont_speak :]
        prefix = self.prefix[self.dont_speak :]

        # Support speaking the full symbol (minus dont_speak).
        self._gen_variations(speakable, symbol, FULL)

        # Now, if you have half-typed a word to narrow down the completion
        # options, support either the full (remaining) symbol, or just the part
        # that is remaining.
        if prefix:
            self._gen_variations(speakable[len(prefix) :], symbol, NOPREFIX)

        # Figure out what shorthand variations are allowed.

        # Now, in case you want to pronounce just until the next symbol, we'll
        # support that shorthand pronunciation.
        shorthand = re.match("^([^0-9._/-]*)[0-9._/-].*$", speakable)
        if shorthand:
            shorthand = shorthand[1]
            self._gen_variations(shorthand, symbol, SHORTHAND)

            # Also support the shorthand of the symbol without the prefix.
            if len(prefix) < len(shorthand):
                self._gen_variations(
                    shorthand[len(prefix) :], symbol, SHORTHAND_NOPREFIX
                )

    def get_talon_list(self):
        """
        Return a talon-list-ready dictionary of pronuncations.

        Any pronunciation with ambiguity or editing required shall return a
        json-encoded result, which must be processed at word-selection-time.
        """
        out = {}
        for speakable, results in self.pronounce.items():
            if len(results) == 1:
                symbol = next(iter(results.keys()))
                if symbol.startswith(self.prefix):
                    # unambiguous choice with no special editing required.
                    out[speakable] = symbol[len(self.prefix) :]
                    continue
            out[speakable] = json.dumps(vars(Edit(prefix=self.prefix, results=results)))
        return out
