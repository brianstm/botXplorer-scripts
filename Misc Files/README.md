# Miscellaneous Files

This Folder contains miscellaneous files that

### way_point.py
It moves the a specified location using the move_base/goal, and then pose it (at the time of making the scipt AMCL wasn't working well, so we had to pose it after every goal, we have now fixed this issue). This was never use as we used a flask app to run it found here [botXplorer-flask-aap](https://github.com/brianstm/botXplorer-flask-app.git).

### move_base_obstacle_detection.py
It runs the move_base and stop it prematurely if the lidar output state is detected, this was made to test out the move_base but was never used.