#!/bin/bash

# Function to run bx command inside the first terminal
run_bx_command() {
    tmux send-keys -t bx-terminal "bx" Enter
}

# Create a new tmux session
tmux new-session -d -s bx-session

# Split the window into four equal parts (top-left, top-right, bottom-left, bottom-right)
tmux split-window -v -t bx-session
tmux split-window -h -t bx-session:0.0
tmux split-window -h -t bx-session:0.2

# Focus on the top-left pane
tmux select-pane -t bx-session:0.0

# Launch terminal on each pane
tmux send-keys -t bx-session:0.0 "gnome-terminal -- /bin/bash" Enter
tmux send-keys -t bx-session:0.1 "gnome-terminal -- /bin/bash" Enter
tmux send-keys -t bx-session:0.2 "gnome-terminal -- /bin/bash" Enter
tmux send-keys -t bx-session:0.3 "gnome-terminal -- /bin/bash" Enter

# Set up the command "bx" to be executed on the first terminal (top-left)
run_bx_command

# Attach to the tmux session to see the result
tmux attach-session -t bx-session