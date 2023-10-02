from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.nix
"""

# As of 22.05: https://nixos.org/manual/nix/stable/language/builtin-constants
builtin_constants = {
    "builtins": "builtins",
    "currentSystem": "current system",
    "currentTime": "current time",
    "false": "false",
    "langVersion": "language version",
    "nixPath": "nix path",
    "nixVersion": "nix version",
    "null": "null",
    "storeDir": "store directory",
    "true": "true",
}

# As of 22.05: https://nixos.org/manual/nix/stable/language/builtins
# TODO: Certain names should also be simplified (ex: generate -> gen)
builtin_functions = {
    "derivation": "derivation",
    "abort": "abort",
    "add": "add",
    "all": "all",
    "any": "any",
    "attrNames": "attribute names",
    "attrValues": "attribute values",
    "baseNameOf": "base name of",
    "builtins": "builtins",
    "catAttrs": "cat attributes",
    "compareVersions": "compare versions",
    "concatLists": "concat lists",
    "concatMap": "concat map",
    "concatStringsSep": "concat strings sep",
    "concatStringsSepMap": "concat strings sep map",
    "deepSeq": "deep sequence",
    "default": "default",
    "derivationStrict": "derivation strict",
    "dirOf": "directory of",
    "div": "div",
    "elem": "element",
    "elemAt": "element at",
    "elemAtOrDefault": "element at or default",
    "elemOrDefault": "element or default",
    "elemPrefix": "element prefix",
    "elemSuffix": "element suffix",
    "elemToPath": "element to path",
    "fetchFromGitHub": "fetch from github",
    "fetchFromGitLab": "fetch from gitlab",
    "fetchTarball": "fetch tarball",
    "filter": "filter",
    "filterSource": "filter source",
    "foldl": "fold left",
    "foldr": "fold right",
    "fromJSON": "from json",
    "functionArgs": "function arguments",
    "functionArgsNames": "function argument names",
    "functionArgsPos": "function argument positions",
    "functionArgsStr": "function argument strings",
    "genList": "generate list",
    "genListLength": "generate list length",
    "getAttr": "get attribute",
    "getEnv": "get environment",
    "getEnvOrDefault": "get environment or default",
    "getFlake": "get flake",
    "getRevision": "get revision",
    "getTarball": "get tarball",
    "getTarballOld": "get tarball old",
    "gettimeofday": "get time of day",
    "hasAttr": "has attribute",
    "hashFile": "hash file",
    "hashString": "hash string",
    "head": "head",
    "import": "import",
    "intersectAttrs": "intersect attributes",
    "isAttrs": "is attributes",
    "isBool": "is boolean",
    "isFloat": "is float",
    "isFunction": "is function",
    "isInt": "is integer",
    "isList": "is list",
    "isNull": "is null",
    "isString": "is string",
    "length": "length",
    "lessThan": "less than",
    "listToAttrs": "list to attributes",
    "map": "map",
    "match": "match",
    "mul": "multiply",
    "parseDrvName": "parse derivation name",
    "pathExists": "path exists",
    "pathLength": "path length",
    "placeholder": "placeholder",
    "readDir": "read directory",
    "readFile": "read file",
    "removeAttrs": "remove attributes",
    "replaceStrings": "replace strings",
    "replaceStringsAll": "replace strings all",
    "seq": "sequence",
    "sha1": "sha1",
    "sha256": "sha256",
    "sha256All": "sha256 all",
    "sort": "sort",
    "split": "split",
    "splitVersion": "split version",
    "storeDir": "store directory",
    "stringLength": "string length",
    "sub": "subtract",
    "substring": "substring",
    "tail": "tail",
    "toFile": "to file",
    "toJSON": "to json",
    "toPath": "to path",
    "toString": "to string",
    "trace": "trace",
    "tryEval": "try evaluate",
    "typeOf": "type of",
    "unsafeDiscardStringContext": "unsafe discard string context",
    "unsafeGetAttrPos": "unsafe get attribute position",
    "unsafeHead": "unsafe head",
    "unsafeTail": "unsafe tail",
    "updateSource": "update source",
    "validate": "validate",
    "writeFile": "write file",
    "zip": "zip",
    "zipAttrs": "zip attributes",
    "zipWith": "zip with",
    "zipWithAttrs": "zip with attributes",
}

system_constants = {
    "x86_64-linux": "X eighty six sixty four linux",
    "x86_64-linux": "X sixty four linux",
    "aarch64-linux": "A arch sixty four linux",
    "aarch64-linux": "arch sixty four linux",
    "x86_64-darwin": "X eighty six sixty four darwin",
    "x86_64-darwin": "X sixty four darwin",
    "aarch64-darwin": "A arch sixty four darwin",
    "aarch64-darwin": "arch sixty four darwin",
}

ctx.lists["user.code_common_function"] = {
    **builtin_functions,
}

ctx.lists["user.code_libraries"] = {}


@mod.capture(rule="{self.nix_functions}")
def lua_functions(m) -> str:
    "Returns a string"
    return m.nix_functions


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
