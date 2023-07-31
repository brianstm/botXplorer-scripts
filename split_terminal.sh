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
