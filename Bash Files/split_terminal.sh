#!/usr/bin/bash

echo "nav - is to turn on all the navigation software (approx. wait time: 60 seconds)"
echo "map - is to turn on all the mapping software (approx. wait time: 80 seconds)"
echo "wifi - is to only initialize the robot for change of wifi (approx. wait time: 30 seconds)"
echo "nil - is to only initialize the robot (approx. wait time: 30 seconds)"
echo "Please type 'nav', 'map' 'wifi' or 'nil' and press Enter:"
read input_choice

SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f2)

TERMINAL_WIDTH=$((SCREEN_WIDTH / 2))
TERMINAL_HEIGHT=$((SCREEN_HEIGHT / 2))

# ORIGINAL_TERMINAL=$(xdotool getactivewindow)
# xdotool windowsize "$ORIGINAL_TERMINAL" ${TERMINAL_WIDTH} ${TERMINAL_HEIGHT}
# xdotool windowmove "$ORIGINAL_TERMINAL" 0 0

if [[ "$input_choice" == "nav" ]]; then
  window_ids=()
  for i in {1..3}; do
    gnome-terminal &
    sleep 0.5
    window_id=$(xdotool search --classname "gnome-terminal" | tail -1)
    window_ids+=("$window_id")
  done

  wmctrl -i -r "${window_ids[0]}" -e "0,0,0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
  wmctrl -i -r "${window_ids[1]}" -e "0,${TERMINAL_WIDTH},0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
  wmctrl -i -r "${window_ids[2]}" -e "0,0,${TERMINAL_HEIGHT},${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"

  xdotool windowactivate --sync "${window_ids[0]}"
  xdotool type "initializing the AMR Robot system"
  xdotool key Return
  xdotool type "bx"
  xdotool key Return

  sleep 2
  xdotool windowactivate --sync "${window_ids[1]}"
  xdotool type "bx"
  sleep 25
  xdotool key Return
  xdotool type "ts"
  sleep 2
  xdotool key Return
  sleep 15
  xdotool type "mb"
  xdotool key Return
  
  sleep 10
  xdotool windowactivate --sync "${window_ids[2]}"
  sleep 2
  xdotool type "rz"
  xdotool key Return
  
elif [[ "$input_choice" == "map" ]]; then
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
  xdotool type "initializing the AMR Robot system"
  xdotool key Return
  xdotool type "bx"
  xdotool key Return

  sleep 2
  xdotool windowactivate --sync "${window_ids[1]}"
  xdotool type "bx"
  sleep 25
  xdotool key Return
  sleep 2
  xdotool type "ts"
  xdotool key Return
  sleep 15
  xdotool type "mpmgm"
  xdotool key Return
  
  sleep 10
  xdotool windowactivate --sync "${window_ids[2]}"
  sleep 2
  xdotool type "mkmap"
  xdotool key Return

  sleep 5
  xdotool windowactivate --sync "${window_ids[3]}"
  sleep 2
  xdotool type "bx"
  xdotool key Return
  sleep 2
  xdotool type "roscd magni_lidar/maps"
  xdotool key Return
  sleep 2
  xdotool type "tt"
  xdotool key Return
  
elif [[ "$input_choice" == "wifi" ]]; then
  window_ids=()
  for i in {1..2}; do
    gnome-terminal &
    sleep 0.5
    window_id=$(xdotool search --classname "gnome-terminal" | tail -1)
    window_ids+=("$window_id")
  done

  wmctrl -i -r "${window_ids[0]}" -e "0,0,0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"
  wmctrl -i -r "${window_ids[1]}" -e "0,${TERMINAL_WIDTH},0,${TERMINAL_WIDTH},${TERMINAL_HEIGHT}"

  xdotool windowactivate --sync "${window_ids[0]}"
  xdotool type "initializing the AMR Robot system"
  xdotool key Return
  xdotool type "bx"
  xdotool key Return

  sleep 2
  xdotool windowactivate --sync "${window_ids[1]}"
  xdotool type "bx"
  sleep 25
  xdotool key Return
  xdotool type "ts"
  xdotool key Return
  
elif [[ "$input_choice" == "nil" ]]; then
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
  xdotool type "initializing the AMR Robot system"
  xdotool key Return
  xdotool type "bx"
  xdotool key Return

  sleep 2
  xdotool windowactivate --sync "${window_ids[1]}"
  xdotool type "bx"
  sleep 25
  xdotool key Return
  xdotool type "ts"
  xdotool key Return

else
  echo "Invalid input. Please type 'nav', 'map', 'wifi' or 'nil."
fi
  echo "Invalid input. Please type 'nav', 'map' or 'nil."
fi
