#!/bin/bash

# Start tmux session with the name "split_terminal"
tmux new-session -d -s split_terminal

# Split the window into 4 equal panes
tmux split-window -v -p 50
tmux split-window -h -p 50
tmux select-pane -t 0
tmux split-window -h -p 50

# Attach to the tmux session
tmux attach-session -t split_terminal