#!/usr/bin/bash

# Check if tmux is installed
if ! command -v tmux &> /dev/null; then
    echo "tmux is not installed. Please install tmux first."
    exit 1
fi

# Create a new tmux session
tmux new-session -d -s split-screen

# Split the window into four equal panes
tmux split-window -v
tmux split-window -h
tmux select-pane -t 0
tmux split-window -h

# Attach to the new session with a split-screen layout
tmux select-layout even-vertical

# Attach to the new session (you will see the four equal panes)
tmux attach-session -t split-screen


# sick@sick:~$ cd /home/sick/Documents/
# sick@sick:~/Documents$ chmod +x split_terminal.sh 
# sick@sick:~/Documents$ ls -l
# total 4
# -rwxrwxrwx 1 sick sick 565 Jul 31 13:46 split_terminal.sh
# sick@sick:~/Documents$ ./split_terminal.sh 
# bash: ./split_terminal.sh: /usr/bin/bash^M: bad interpreter: No such file or directory
# sick@sick:~/Documents$ bash ./split_terminal.sh 
# ./split_terminal.sh: line 2: $'\r': command not found
# ./split_terminal.sh: line 23: syntax error: unexpected end of file
# sick@sick:~/Documents$ 

