# also useful for C programming, but for now i just enable it for gdb
tag: user.gdb
-
cast to <user.datatype>: "{datatype}"
(de ref | dereference) [cast to] <user.datatype>: "*{datatype}"

mask (byte | eight bits): "& 0xff"
mask (word | sixteen bits): "& 0xffff"
mask (d word | thirty two bits): "& 0xffffffff"
mask (cue word | sixty four bits): "& 0xffffffffffffffff"
