#!/usr/bin/bash

# Function to run bx command inside the first terminal
run_bx_command() {
    gnome-terminal --geometry=${TERMINAL_WIDTH}x${TERMINAL_HEIGHT}+0+0 -- /bin/bash -c "bx; exec bash"
}

# Get the screen width and height
SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f2)

# Calculate the dimensions for each terminal window
TERMINAL_WIDTH=$((SCREEN_WIDTH / 2))
TERMINAL_HEIGHT=$((SCREEN_HEIGHT / 2))

# Launch four terminal windows
gnome-terminal &
gnome-terminal &
gnome-terminal &
gnome-terminal &

# Give some time for the terminals to open
sleep 2

# Move and resize the terminal windows
xdotool search --classname "gnome-terminal" windowmove 0 0
xdotool search --classname "gnome-terminal" windowsize ${TERMINAL_WIDTH} ${TERMINAL_HEIGHT}
xdotool getactivewindow windowmove ${TERMINAL_WIDTH} 0
xdotool search --classname "gnome-terminal" windowmove 0 ${TERMINAL_HEIGHT}
xdotool search --classname "gnome-terminal" windowmove ${TERMINAL_WIDTH} ${TERMINAL_HEIGHT}

# Run the bx command in the first terminal
run_bx_command