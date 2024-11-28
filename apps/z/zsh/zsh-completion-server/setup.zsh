# Handle an incoming socket connection.
_conn_handler () {
    local REPLY
    # Accept a connection from the listener fd.
    zsocket -a $1
    # Connect the connection fd to the _data_handler.
    zle -F "$REPLY" _data_handler
    # Remember this fd for push requests.
    _zsh_completion_server_last_conn_fd="$REPLY"
}

# Handle data coming on a socket.  Note that this will only ever trigger while
# zle is awaiting input on the tty (that is, at the zsh prompt).  Requests sent
# at any other time may block for as long as the active command takes to run.
_data_handler () {
    local line
    if ! read -r line <&$1; then
        # Error handling.
        # I have no clue what this line is for, it's in man zshzle
        zle -F $1
        return 1
    fi
    # XXX - add support for different commands, such as directory completion
    _completion_request "$1" "$line"
}

# Define how we respond to data on the socket
_completion_request () {
    # We get the fd of the socket and the content of the request line:
    local fd="$1"
    local line="$2"

    if [ -z "$fd" ] ; then
        fd="$_zsh_completion_server_last_conn_fd"
        line="$(echo "key")"
    fi

    # Call a zsh-completion-request script on the PATH if one exists
    if which zsh-completion-request >/dev/null ; then
        # Call the modified zsh4humans code.
        local REPLY_CONTEXT
        local REPLY_PREFIX
        local -a REPLY_WORDS
        z4h-fzf-complete
        # Feed each completion results to talon via a file descriptor.
        (
            echo "completions"
            echo - "$REPLY_CONTEXT"
            echo - "$REPLY_PREFIX"
            for word in $REPLY_WORDS; do
                echo - $word
            done
            echo "::done::"
        ) >&"$1"
    fi
}

### End function definitions

# Get the absolute path to this file (assume we are being sourced).
dir="$(dirname "$(readlink -f $0)")"

# Include ./fn in fpath and autoload the files
fpath=("$dir"/fn $fpath)
autoload -U "$dir"/fn/*(:t)

zmodload zsh/net/socket

# Create the unix socket for the connection.
mkdir -p "$dir/sock"
sockfile="$dir/sock/$$.sock"
rm -f "$sockfile"

# Create a unix socket listener.
zsocket -l "$sockfile"

# Connect the listner fd to the _conn_handler.
zle -F $REPLY _conn_handler

# Every zsh prompt sets the X11 window title to "zsh:PID:PWD".  This allows the
# zsh-completion-server to be found by X11 tools whenever zsh is active.
function _set_zsh_title () {
    echo -ne '\x1bkzsh:'"$$:$PWD"'\x1b\'
}
precmd_functions+=_set_zsh_title

# Erase the zsh title when we execute anything else, so nothing tries to
# interact with the completion server while it is dormant.  Otherwise, the
# second or third attempt to connect to the completion server will hang forever.
function _set_cmd_title () {
    echo -ne '\x1bk'"$1"'\x1b\'
}
preexec_functions+=_set_cmd_title


# push completion to the server without it having asked for it
# This can be bound to a key.
_push_request () {
    # If we have no recent connections.. ignore the request.
    if [ -z "$_zsh_completion_server_last_conn_fd" ] ; then
        return
    fi
    _completion_request "$_zsh_completion_server_last_conn_fd" "$(echo "key")"
}

# Allow triggering via a keybinding in addition to the socket input.
zle -N _push_request
bindkey '^T' _push_request
bindkey '^G' list-choices

unset dir REPLY sockfile
