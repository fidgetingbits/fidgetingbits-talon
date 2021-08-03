tag: user.libptmalloc
-

tag(): user.heap_analysis

# XXX - eventually these could be replaced with generic heap actions
heck stump <number> chunks: "ptchunk -x -c {number} "
search <number> chunks: "ptchunk -c {number} -s"
# XXX - rename these
fast bins: "ptfast "
tea cache: "pttcache "
free bins: "ptbin "
small bins: "ptbin "
chunk meta: "ptmeta "
chunk config: "ptconfig "
chunk set config: "ptconfig -v "
heap info: "ptparam\n"

P T chunk help: "ptchunk -h\n"
P T list help: "ptlist -h\n"
P T list: "ptlist "
P T list tag trace: "ptlist -M 'tags, backtrace:3' "
P T list save: "ptlist -M 'tags, backtrace:3' --json "
P T debug: "--loglevel debug"

P T arena list only: "ptarena -l\n"

print main arena: "p &main_arena\n"
