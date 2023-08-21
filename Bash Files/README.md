# Bash Files

This Folder contains the bash and sh files for the Virtual Machine

## Usage
It will open the terminal in a split screen and will initialize the AMR.

### split_terminal_test.sh
scripting language commands file to test out the tmux, but it doesn't work as expected.

### split_terminal.sh
Scripting language commands file to prompt user with options and run the terminal splitting as options using the wmctrl to open and size the terminal and xdotool to type in the commands.

### split_terminal.desktop
Desktop file to run the scripting command files above making it to a executable. Note: change the Exec to your file location, and the Icon to be your icon (if any), or else you can use linux's basic icons like e.g., terminal.