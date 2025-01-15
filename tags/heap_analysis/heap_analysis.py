from talon import Context, Module

ctx = Context()
ctx.matches = r"""
tag: user.heap_analysis
"""
mod = Module()
mod.tag(
    "heap_analysis", desc="Tag for enabling generic heap analysis debugger commands"
)


@mod.action_class
class Actions:
    def heap_analysis_chunk():
        """analyze a chunk on the heap"""

    def heap_analysis_chunk_verbose():
        """analyze a chunk on the heap, passing verbose flags"""

    def heap_analysis_chunk_hexdump():
        """analyze a chunk on the heap, passing hexdump flags"""

    def heap_analysis_chunk_help():
        """chunk analysis help"""

    def heap_analysis_search():
        """search the contents of a chunk"""

    def heap_analysis_arena():
        """analyze a heaps arena"""

    def heap_analysis_arena_list():
        """analyze a heaps arena"""

    def heap_analysis_bin():
        """analyze a heaps bin"""

    def heap_analysis_call_back():
        """manage heap callbacks"""

    def heap_analysis_arena_of():
        """XXX"""

    def heap_analysis_scan():
        """scan the contents of the heap"""

    def heap_analysis_help():
        """help menu for the heap analysis plugin"""
