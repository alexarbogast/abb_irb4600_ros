# abb_irb4600_robot

This package provides configuration and launch files for running the ABB IRB
4600 in **simulation** and (eventually) on the **physical hardware**.

## Running the Robot

The [abb_irb4600_robot.launch.py](./launch/abb_irb4600_robot.launch.py) file
will launch the hardware interface and controllers.

```shell
ros2 launch abb_irb4600_robot abb_irb4600_robot.launch
```

By default, this launches the robot with a joint position trajectory controller.
A different controller can be launched by first adding the controller parameters
to the parameter server and then passing the name of the controller via the
`controller` argument.

Rviz is disabled by default. Use `rviz:=true` to visualize the robot. This is
done to prevent overlapping Rviz windows when using MoveIt.

## Motion planning with MoveIt

Rviz can be used for interactive motion planning with MoveIt.
In another terminal:

```shell
ros2 launch abb_irb4600_robot moveit_planning.launch
```
