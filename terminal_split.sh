#!/usr/bin/bash

SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f2)

TERMINAL_WIDTH=$((SCREEN_WIDTH / 2))
TERMINAL_HEIGHT=$((SCREEN_HEIGHT / 2))

# ORIGINAL_TERMINAL=$(xdotool getactivewindow)
# xdotool windowsize "$ORIGINAL_TERMINAL" ${TERMINAL_WIDTH} ${TERMINAL_HEIGHT}
# xdotool windowmove "$ORIGINAL_TERMINAL" 0 0

window_ids=()
for i in {1..4}; do
  gnome-terminal &
  sleep 0.5
  window_id=$(xdotool search --classname "gnome-terminal" | tail -1)
  window_ids+=("$window_id")
done

wmctrl -i -r "${window_ids[0]}" -e "0,0,0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
wmctrl -i -r "${window_ids[1]}" -e "0,${TERMINAL_WIDTH},0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
wmctrl -i -r "${window_ids[2]}" -e "0,0,${TERMINAL_HEIGHT},${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
wmctrl -i -r "${window_ids[3]}" -e "0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT},${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"

xdotool windowactivate --sync "${window_ids[0]}"
xdotool type "initiallizing the AMR Robot system"
xdotool key Return
xdotool type "bx"
xdotool key Return

xdotool windowactivate --sync "${window_ids[1]}"

[ WARN] [1690861195.156498128]: Control loop missed its desired rate of 5.0000Hz... the loop actually took 0.2026 seconds
[ WARN] [1690861195.346218475]: Map update loop missed its desired rate of 5.0000Hz... the loop actually took 0.2021 seconds
[ WARN] [1690861195.582957311]: Control loop missed its desired rate of 5.0000Hz... the loop actually took 0.2291 seconds
[ WARN] [1690861195.880729960]: TebLocalPlannerROS: trajectory is not feasible. Resetting planner...
[ WARN] [1690861201.196500579]: Map update loop missed its desired rate of 1.0000Hz... the loop actually took 4.8882 seconds
[ WARN] [1690861201.354069182]: Clearing both costmaps outside a square (3.00m) large centered on the robot.
[ WARN] [1690861204.588422646]: Map update loop missed its desired rate of 1.0000Hz... the loop actually took 2.3919 seconds
