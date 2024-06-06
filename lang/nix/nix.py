from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: nix
"""

mod.list("nix_builtin_keywords", desc="List of Nix builtin keywords")
mod.list("nix_builtins_functions", desc="List of Nix builtins functions")
mod.list("nix_lib_functions", desc="List of Nix library functions")
mod.list("nix_pkgs_functions", desc="List of Nix nixpkgs functions")
mod.list("nix_types", desc="List of Nix option types")
mod.list("nix_libs", desc="List of Nix libraries")

nix_libs = {
    "lib": "lib",
    "builtins": "builtins",
    "packages": "pkgs",
}

# I try to use library prefixes to keep with best practices, which try to avoid `with` as well as `builtins`, were
# necessary. However I also favor brevity, so for for example for something that is defined in lib.strings, but that is
# also alias in lib, a favor lib. If you want a good reference for this type of thing check out noogle.dev.


# As of 22.05: https://nixos.org/manual/nix/stable/language/builtin-constants
builtin_constants = {
    "builtins": "builtins",
    "current system": "currentSystem",
    "current time": "currentTime",
    "false": "false",
    "language version": "langVersion",
    "nix path": "nixPath",
    "nix version": "nixVersion",
    "null": "null",
    "store directory": "storeDir",
    "true": "true",
}

# As of 22.05: https://nixos.org/manual/nix/stable/language/builtins
# TODO: Certain names should also be simplified (ex: generate -> gen)
# FIXME: A lot of these are preferred to be called through lib, so should move.
# Can use noogle.dev to quickly check which are aliased through lib.
builtin_functions = {
    "derivation": "derivation",
    "abort": "abort",
    "add": "add",
    "all": "all",
    "any": "any",
    "attribute names": "attrNames",
    "attribute values": "attrValues",
    "base name of": "baseNameOf",
    "cat attributes": "catAttrs",
    "compare versions": "compareVersions",
    "concat lists": "concatLists",
    "concat map": "concatMap",
    "concat strings sep": "concatStringsSep",
    "concat strings sep map": "concatStringsSepMap",
    "deep sequence": "deepSeq",
    "default": "default",
    "derivation strict": "derivationStrict",
    "directory of": "dirOf",
    "div": "div",
    "element": "elem",
    "element at": "elemAt",
    "element at or default": "elemAtOrDefault",
    "element or default": "elemOrDefault",
    "element prefix": "elemPrefix",
    "element suffix": "elemSuffix",
    "element to path": "elemToPath",
    "fetch from github": "fetchFromGitHub",
    "fetch from gitlab": "fetchFromGitLab",
    "fetch tarball": "fetchTarball",
    "filter": "filter",
    "filter source": "filterSource",
    "fold left": "foldl",
    "fold right": "foldr",
    "from json": "fromJSON",
    "function arguments": "functionArgs",
    "function argument names": "functionArgsNames",
    "function argument positions": "functionArgsPos",
    "function argument strings": "functionArgsStr",
    "generate list": "genList",
    "generate list length": "genListLength",
    "get attribute": "getAttr",
    "get environment": "getEnv",
    "get environment or default": "getEnvOrDefault",
    "get flake": "getFlake",
    "get revision": "getRevision",
    "get tarball": "getTarball",
    "get tarball old": "getTarballOld",
    "get time of day": "gettimeofday",
    "has attribute": "hasAttr",
    "hash file": "hashFile",
    "hash string": "hashString",
    "head": "head",
    "import": "import",
    "intersect attributes": "intersectAttrs",
    "is attributes": "isAttrs",
    "is boolean": "isBool",
    "is float": "isFloat",
    "is function": "isFunction",
    "is integer": "isInt",
    "is list": "isList",
    "is null": "isNull",
    "is string": "isString",
    "length": "length",
    "less than": "lessThan",
    "list to attributes": "listToAttrs",
    "map": "map",
    "match": "match",
    "multiply": "mul",
    "parse derivation name": "parseDrvName",
    "path exists": "pathExists",
    "path length": "pathLength",
    "placeholder": "placeholder",
    "read directory": "readDir",
    "read file": "readFile",
    "remove attributes": "removeAttrs",
    "replace strings": "replaceStrings",
    "replace strings all": "replaceStringsAll",
    "sequence": "seq",
    "sha1": "sha1",
    "sha256": "sha256",
    "sha256 all": "sha256All",
    "sort": "sort",
    "split": "split",
    "split version": "splitVersion",
    "store directory": "storeDir",
    "string length": "stringLength",
    "subtract": "sub",
    "substring": "substring",
    "tail": "tail",
    "to file": "toFile",
    "to json": "toJSON",
    "to path": "toPath",
    "to string": "toString",
    "trace": "trace",
    "try evaluate": "tryEval",
    "type of": "typeOf",
    "unsafe discard string context": "unsafeDiscardStringContext",
    "unsafe get attribute position": "unsafeGetAttrPos",
    "unsafe head": "unsafeHead",
    "unsafe tail": "unsafeTail",
    "update source": "updateSource",
    "validate": "validate",
    "write file": "writeFile",
    "zip": "zip",
    "zip attributes": "zipAttrs",
    "zip with": "zipWith",
    "zip with attributes": "zipWithAttrs",
}

# FIXME: One of many dicts to change to having variable dictation, ex: (list to addrs|list to attributes)
lib_functions = {
    "list to adders": "listToAttrs",
    "adder by path": "attrByPath",
    "make default": "mkDefault",
    "make option": "mkOption",
    "make option default": "mkOptionDefault",
    "make option type": "mkOptionType",
}

stdenv_functions = {
    "make derivation": "mkDerivation",
}

# Incomplete, but the most common
pkgs_functions = {
    "fetch from github": "fetchFromGitHub",
    "fetch from gitlab": "fetchFromGitLab",
    "fetch tarball": "fetchTarball",
    "fetch zip": "fetchzip",
    "fetch from url": "fetchurl",
    "fetch from svn": "fetchsvn",
    "fetch url": "fetchurl",
    "fetch git": "fetchgit",
    "fetch debian patch": "fetchDebianPatch",
    "fetch yarn deps": "fetchYarnDeps",
    "fetch patch": "fetchpatch",
    "fetch docker": "fetchdocker",
}

system_constants = {
    "X sixty four linux": "x86_64-linux",
    "arch sixty four linux": "aarch64-linux",
    "X sixty four darwin": "x86_64-darwin",
    "arch sixty four darwin": "aarch64-darwin",
}


ctx.lists["user.nix_builtin_keywords"] = {**builtin_constants, **system_constants}

ctx.lists["user.nix_builtins_functions"] = {
    **builtin_functions,
}

ctx.lists["user.nix_lib_functions"] = {**lib_functions}

ctx.lists["user.nix_pkgs_functions"] = {**pkgs_functions}

ctx.lists["user.code_common_function"] = {
    **builtin_functions,
}

ctx.lists["user.code_libraries"] = {}

ctx.lists["user.nix_libs"] = nix_libs

# https://nixos.org/manual/nixos/stable/#sec-option-types
option_types = {
    # Basic types
    "bool": "bool",
    "bool by or": "boolByOr",
    "path": "path",
    "path in store": "pathInStore",
    "package": "package",
    # FIXME: This contains actual values like enum [ "left" "right" ], so may need special case
    "enum": "enum ",
    "anything": "anything",
    "raw": "raw",
    "option type": "optionType",
    # attrs omitted because it's deprecated
    "packages": "pkgs",
    # Numeric types
    "integer": "int",
    # FIXME: Maybe tweak these names D word is meh
    "signed byte": "ints.s8",
    "signed word": "ints.s16",
    "signed D word": "ints.s32",
    "unsigned": "ints.unsigned",
    "unsigned byte": "ints.u8",
    "unsigned word": "ints.u16",
    "unsigned D word": "ints.u32",
    "int between": "ints.between ",
    "int positive": "ints.positive",
    "port": "ints.port",
    "float": "float",
    "numb": "number",
    "numb between": "numbers.between",
    "non negative": "numbers.nonNegative",
    "numb positive": "numbers.positive",
    # String types
    "string": "str",
    # FIXME: This has arguements too
    "separated string": "separatedString",
    "lines": "lines",
    "commas": "commas",
    "env vars": "envVar",
    "stir matching": "strMatching",
    # Submodule types
    "submodule": "submodule",
    "submodule with": "submoduleWith",
    "deferred module": "deferredModule",
    # Composed types
    "list of": "listOf",
    "attrs of": "attrs of",
    "lazy attrs of": "lazyAttrsOf",
    "null or": "nullOr",
    "unique": "uniq",
    "unique message": "unique { }",
    "either": "either",
    "one of": "oneOf",
    "coerced to": "coercedTo",
}
ctx.lists["user.nix_types"] = option_types


@mod.capture(rule="{self.nix_types}")
def nix_types(m) -> str:
    "Returns an option typed prefixed with 'lib.types.'"
    return f"lib.types.{m.nix_types}"


@mod.capture(rule="{self.nix_builtins_functions}")
def nix_builtins_functions(m) -> str:
    "Returns a string"
    return f"builtins.{m.nix_builtins_functions}"


@mod.capture(rule="{self.nix_lib_functions}")
def nix_lib_functions(m) -> str:
    "Returns a string"
    return f"lib.{m.nix_lib_functions}"


@mod.capture(rule="{self.nix_pkgs_functions}")
def nix_pkgs_functions(m) -> str:
    "Returns a string"
    return f"pkgs.{m.nix_pkgs_functions}"


@mod.capture(
    rule="(<self.nix_builtins_functions>|<self.nix_lib_functions><self.nix_pkgs_functions>)"
)
def nix_functions(m) -> str:
    "Returns a string"
    return m


# This is useful for `with lib` or `with builtins` statements
@mod.capture(
    rule="({self.nix_builtins_functions}|{self.nix_lib_functions}|{self.nix_pkgs_functions})"
)
def nix_raw_functions(m) -> str:
    "Returns a string"
    return m


@ctx.action_class("user")
class UserActions:
    # tag-related actions listed first, indicated by comment. corresponds to
    # the tag(): user.code_imperative style declaration in the language .talon
    # file

    ##
    # code_imperative
    ##
    def code_state_if():
        actions.user.insert_between("if ", " then")

    def code_state_else():
        actions.insert("else\n")

    ##
    # code_comment_line
    ##
    def code_comment_line_prefix():
        actions.insert("# ")

    def code_comment_block():
        actions.insert(
            f"{actions.user.code_comment_block_prefix()}\n\n{actions.user.code_comment_block_suffix()}"
        )
        actions.edit.up()

    def code_comment_block_prefix():
        actions.auto_insert("/*")

    def code_comment_block_suffix():
        actions.auto_insert("*/")

    ##
    # code_data_bool
    ##
    def code_insert_true():
        actions.insert("true")

    def code_insert_false():
        actions.insert("false")

    ##
    # code_data_null
    ##
    def code_insert_null():
        actions.insert("null")

    def code_insert_is_null():
        actions.insert(" == null")

    def code_insert_is_not_null():
        actions.insert(" != null")

    ##
    # code_functions
    ##
    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "{} = {{}}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.key("left:1")
        actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        actions.user.code_private_function(text)

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    ##
    # code_libraries
    ##
    def code_import():
        actions.user.insert("import ")

    ##
    # code_libraries_gui
    ##
    def code_insert_library(text: str, selection: str):
        actions.insert(f"local {selection} = require('{selection}')")

    ##
    # code_operators_array
    ##
    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    ##
    # code_operators_assignment
    ##
    def code_operator_assignment():
        actions.insert(" = ")

    ##
    # code_operators_math
    ##
    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_division():
        actions.insert(" / ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" = ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    def code_operator_and():
        actions.insert(" and ")

    def code_operator_or():
        actions.insert(" or ")

    ###
    # code_operators_bitwise
    ###
    # TODO: These will need to use builtins

    # non-tag related actions
