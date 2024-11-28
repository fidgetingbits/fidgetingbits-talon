# these commands are for the following gdb plugin
# https://github.com/cloudburst/libheap
tag: user.heapls
-

[run] heap: "heap\n"
heap help$: "heap -h\n"
heap list: "heapls\n"
fast bins$: "fastbins\n"
fast bins <number>: "fastbins {number}\n"
small bins$: "smallbins\n"
small bins <number>: "smallbins {number}\n"
free bins: "freebins\n"
compact heap list: "heaplsc\n"
heap stats: "mstats\n"
