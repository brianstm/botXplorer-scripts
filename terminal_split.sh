#!/usr/bin/bash

# Function to run a command in a terminal
function run_command_in_terminal() {
    local command=$1
    local title=$2
    gnome-terminal --title="$title" -- bash -c "$command; exec bash"
}

# Function to split the screen into 4 equal parts and run commands in each terminal
function split_screen_and_run_commands() {
    local command1="bx" # Command to run in the top-left terminal
    local command2=""   # Command to run in the top-right terminal
    local command3=""   # Command to run in the bottom-left terminal
    local command4=""   # Command to run in the bottom-right terminal

    # Calculate the screen dimensions
    local screen_width=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1)
    local screen_height=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2)

    # Calculate the dimensions for each terminal
    local terminal_width=$((screen_width / 2))
    local terminal_height=$((screen_height / 2))

    # Run the commands in separate terminals
    run_command_in_terminal "$command1" "Top-Left Terminal" &
    run_command_in_terminal "$command2" "Top-Right Terminal" &
    run_command_in_terminal "$command3" "Bottom-Left Terminal" &
    run_command_in_terminal "$command4" "Bottom-Right Terminal" &
}

# Call the function to split the screen and run commands
split_screen_and_run_commands
