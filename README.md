# abb_irb4600_ros

**ROS integration for the ABB IRB 4600 series manipulator**

<p align="center">
  <img src=https://github.com/alexarbogast/abb_irb4600_description/assets/46149643/08e91f96-9ef0-455e-9b88-d4b86603e103 width=250/>
</p>

## Contents

- [Installation](#1)
- [Simulating the robot in ROS 2](#2)
- [RobotStudio Simulation](#3)

<a id='1'></a>

## Installation

Create a ROS 2 workspace and clone this package into a `src` directory.

Import package dependencies for this package and the robot driver `abb_ros2`:

```bash
sudo apt update
rosdep update
cd src
vcs import < abb_irb4600_ros/abb.repos
vcs import < abb_ros2/abb.repos
rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

Build the packages:

```bask
cd <COLCON_WORKSPACE>
colcon build
```

<a id='2'></a>

## Simulating the robot in ROS 2

The `abb_irb4600_robot` package contains a set of launch files for running the
robot. RobotStudio is not required if the simulation is running exclusively in
ROS, without the `abb_ros2` driver. The launch file uses this configuration by
default.

The [robot_bringup.launch.py](./launch/robot_bringup.launch.py) file will launch
the hardware interface and controllers.

```shell
ros2 launch abb_irb4600_robot robot_bringup.launch.py rviz:=false
```

By default, this launches the robot with a joint position trajectory controller.
A different controller can be launched by first adding the controller parameters
to the parameter server and then passing the name of the controller via the
`controller` argument.

Rviz is disabled by default. Use `rviz:=true` to visualize the robot. This is
done to prevent overlapping Rviz windows when using MoveIt.

Launch MoveIt to perform motion planning.

```shell
ros2 launch abb_irb4600_robot moveit_planning.launch.py
```

<a id='3'></a>

## RobotStudio Simulation

Setup
[robot studio](https://github.com/PickNikRobotics/abb_ros2/blob/rolling/docs/RobotStudioSetup.md)
and
[configure the network settings](https://github.com/PickNikRobotics/abb_ros2/blob/rolling/docs/NetworkingConfiguration.md)
according to the instructions provided with the driver.

To launch the robot using the `ABBSystemHardware` provided by the driver, set
the `use_mock_hardware:=false` and `rws_ip:=<ROBOTSTUDIO_IP>`, substituting
`<ROBOTSTUDIO_IP>` with the IP of the computer running RobotStudio.

```shell
ros2 launch abb_irb4600_robot robot_bringup.launch.py rviz:=false use_mock_hardware:=false rws_ip:=<ROBOTSTUDIO_IP>
```

Launch MoveIt to perform motion planning.

```shell
ros2 launch abb_irb4600_robot moveit_planning.launch.py
```

When executing a motion plan. The robot should move in RobotStudio.
