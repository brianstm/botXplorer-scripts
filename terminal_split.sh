#!/bin/bash

# Function to run bx command inside the first terminal
run_bx_command() {
    gnome-terminal -- /bin/bash -c "bx; exec bash"
}

# Function to arrange terminal windows on the screen
arrange_terminals() {
    sleep 1 # Give some time for terminal windows to open
    wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz
    wmctrl -r :ACTIVE: -e 0,0,0,$((SCREEN_WIDTH/2)),$((SCREEN_HEIGHT/2))
    wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
    wmctrl -r :ACTIVE: -b remove,maximized_vert
    wmctrl -r :ACTIVE: -e 0,$((SCREEN_WIDTH/2)),0,$((SCREEN_WIDTH/2)),$((SCREEN_HEIGHT/2))
    wmctrl -r :ACTIVE: -b add,maximized_vert
    wmctrl -r :ACTIVE: -b remove,maximized_horz
    wmctrl -r :ACTIVE: -e 0,0,$((SCREEN_HEIGHT/2)),$((SCREEN_WIDTH/2)),$((SCREEN_HEIGHT/2))
    wmctrl -r :ACTIVE: -b add,maximized_horz
}

# Get the screen width and height
SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f2)

# Launch four terminal windows
gnome-terminal &
gnome-terminal &
gnome-terminal &
gnome-terminal &

# Run bx command in the first terminal
run_bx_command

# Arrange terminal windows on the screen
arrange_terminals