app: terminal
tag: terminal
-

(program|file) trace: user.trace_program()
(program|file) trace [with] filter [{user.tracing_filters}]: user.trace_program_with_filter(tracing_filters or "")
(program|file) trace path: user.trace_program_with_path()
(program|file) trace log: user.trace_program_with_log()
trace (that|this):
    edit.line_start()
    user.trace_program()
trace last:
    edit.line_up()
    edit.line_start()
    user.trace_program()
