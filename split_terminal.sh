#!/usr/bin/bash

# Start tmux session with the name "split_terminal"
tmux new-session -d -s split_terminal

# Split the window into 4 panes
tmux split-window -h -p 50
tmux split-window -v -p 50
tmux select-pane -t 0
tmux split-window -v -p 50

# Move to the top-left pane and split it horizontally
tmux select-pane -t 0
tmux split-window -h -p 50

# Rearrange the panes
tmux select-pane -t 2
tmux swap-pane -U
tmux select-pane -t 0
tmux swap-pane -L

# Attach to the tmux session
tmux attach-session -t split_terminal