from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.libptmalloc
"""


@ctx.action_class("user")
class UserActions:
    def heap_analysis_chunk():
        actions.auto_insert("ptchunk ")

    def heap_analysis_chunk_verbose():
        actions.auto_insert("ptchunk -v")

    def heap_analysis_chunk_hexdump():
        actions.auto_insert("ptchunk -x")

    def heap_analysis_chunk_help():
        actions.auto_insert("ptchunk -h\n")

    def heap_analysis_search():
        actions.auto_insert("ptsearch ")

    def heap_analysis_arena():
        actions.auto_insert("ptarena ")

    def heap_analysis_arena_list():
        actions.auto_insert("ptlist ")

    def heap_analysis_bin():
        actions.auto_insert("ptbin ")

    def heap_analysis_call_back():
        actions.auto_insert("ptcallback ")

    def heap_analysis_arena_of():
        actions.auto_insert("ptarenaof ")

    def heap_analysis_scan():
        actions.auto_insert("ptscanchunks ")

    def heap_analysis_help():
        actions.auto_insert("pthelp\n")
