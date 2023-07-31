#!/bin/bash

# Function to run bx command inside the first terminal
run_bx_command() {
    gnome-terminal -- /bin/bash -c "bx; exec bash"
}

# Get the screen width and height
SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f2)

# Calculate the dimensions for each terminal window
TERMINAL_WIDTH=$((SCREEN_WIDTH / 2))
TERMINAL_HEIGHT=$((SCREEN_HEIGHT / 2))

# Launch four terminal windows with custom geometry
gnome-terminal --geometry=${TERMINAL_WIDTH}x${TERMINAL_HEIGHT}+0+0 &
gnome-terminal --geometry=${TERMINAL_WIDTH}x${TERMINAL_HEIGHT}+${TERMINAL_WIDTH}+0 &
gnome-terminal --geometry=${TERMINAL_WIDTH}x${TERMINAL_HEIGHT}+0+${TERMINAL_HEIGHT} &
gnome-terminal --geometry=${TERMINAL_WIDTH}x${TERMINAL_HEIGHT}+${TERMINAL_WIDTH}+${TERMINAL_HEIGHT} &

# Run bx command in the first terminal
run_bx_command