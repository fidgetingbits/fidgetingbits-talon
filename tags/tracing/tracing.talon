tag: terminal
-

(program|file) trace: user.trace_program()
(program|file) trace [with] filter [{user.tracing_filters}]: user.trace_program_with_filter(tracing_filters or "")
(program|file) trace path: user.trace_program_with_path()
(program|file) trace log: user.trace_program_with_log()
