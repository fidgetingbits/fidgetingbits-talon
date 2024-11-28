# For linux kernel debugging
# See https://www.kernel.org/doc/Documentation/dev-tools/gdb-kernel-debugging.rst
tag: user.gdb_vmlinux
-

# commands from apropros lx

#(gdb) apropos lx
#function lx_current -- Return current task.
#function lx_module -- Find module by name and return the module variable.
#function lx_per_cpu -- Return per-cpu variable.
#function lx_rb_first -- Lookup and return a node from an RBTree
#function lx_rb_last -- Lookup and return a node from an RBTree.
#function lx_rb_next -- Lookup and return a node from an RBTree.
#function lx_rb_prev -- Lookup and return a node from an RBTree.
#function lx_task_by_pid -- Find Linux task by PID and return the task_struct variable.
#function lx_thread_info -- Calculate Linux thread_info from task variable.
#function lx_thread_info_by_pid -- Calculate Linux thread_info from task variable found by pid
#lx-configdump -- Output kernel config to the filename specified as the command
#lx-cpus -- List CPU status arrays
#lx-dmesg -- Print Linux kernel log buffer.
#lx-list-check -- Verify a list consistency
#lx-lsmod -- List currently loaded modules.
#lx-ps -- Dump Linux tasks.
#lx-symbols -- (Re-)load symbols of Linux kernel and currently loaded modules.

lux help: insert("apropos lx\n")
lux config dump: insert("lx-configdump\n")
lux see pee ewes: insert("lx-cpus\n")
lux D message: insert("lx-dmesg\n")
lux list check: insert("lx-list-check ")
lux (modules | module list): insert("lx-lsmod\n")
lux process list: insert("lx-ps\n")
lux symbols: insert("lx-symbols\n")

lux current: "call $lx_current()\n"
lux task:
    insert('printf "name: %s\\npid: %d\\n", $lx_current()->comm, $lx_current()->pid\n')
