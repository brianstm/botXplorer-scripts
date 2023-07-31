#!/bin/bash

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

# Position and resize the terminal windows
window_list=$(xdotool search --classname "gnome-terminal")

for window_id in $window_list; do
    xdotool windowmove $window_id 0 0
    xdotool windowsize $window_id ${TERMINAL_WIDTH} ${TERMINAL_HEIGHT}
    xdotool windowactivate $window_id
    sleep 0.5
done

# Run the bx command in the first terminal
run_bx_command