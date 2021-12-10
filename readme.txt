ENPM 662 - PROJECT 2
Instructions to Run the project:

1) Download all the files in your catkin workspace src folder
2) Change the directory to catkin workspace using "cd ~/catkin_ws
3) Run catkin_make clean && catkin_make
4) If some of the packages couldn't build, make sure to download the ydlidar and ros controllers from their website. 
Note that these packages are essential resources to the main project and they were pulled from the original github repositories of ydlidar and ros controllers.
5) After successful cmake, now launch the project using:
	roslaunch trial5_assembly just_controller.launch
6) To run the teleop:
	Open a new terminal and run:
		rosrun project2_control move_forward.py
		The Keys are:
		
	Moving Around:
	--------------------
	      w
	  a       s
	      d

	  Space Bar
  
	spacebar: stop the vehicle abruptly
	longpress w: increase the forward velocity
	longpress d: decrease the velocity and move backward
	longpress a: move to the left 
	longpress s: move to the right
	z - back bend
	q - back up
	e - front up
	c - frend bend
	1 - front left knee lift
	2 - front left knee down
	3 - front right knee lift
	4 - front right knee down
	5 - back left knee lift
	6 - back left knee down
	7 - back right knee lift
	8 - back right knee down
	r - front left hip lift
	f - front left hip down
	t - front right hip lift
	g - front right hip down
	y - back left hip lift
	h - back left hip down
	u - back right hip lift
	j - back right hip down
	o - initial position
	b - make front joint angles equal to one of the front legs and back joint angles equal to one of the back legs
	
7) To run inverse kinematics validation:
	Moving the front right leg in half sinusoidal wave motion = |sinx|:
		rosrun project2_control validation.py
