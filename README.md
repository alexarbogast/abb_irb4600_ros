# abb_irb4600_ros

**ROS integration for the ABB IRB 4600 series manipulator**

<p align="center">
  <img src=https://github.com/alexarbogast/abb_irb4600_description/assets/46149643/08e91f96-9ef0-455e-9b88-d4b86603e103 width=250/>
</p>

## Contents

- [Installation](#1)
- [Dependencies](#2)
- [Running the Robot](#3)

<a id='1'></a>

## Installation

Clone the repository to your local workspace. If you do not already have the
[abb_irb4600_description](https://github.com/alexarbogast/abb_irb4600_description)
package, you will need to clone recursively.

```shell
mkdir catkin_ws/src && cd catkin_ws/src
git clone --recurse-submodules git@github.com:alexarbogast/abb_irb4600_ros.git
```

Build your workspace

```shell
catkin build
```

<a id='2'></a>

## Dependencies

Running the _physical robot_ will require the
[abb_robot_driver](https://github.com/ros-industrial/abb_robot_driver), but the
integration of the driver into the hardware package is a work in progress.

For now,
[ros_control_boilerplate](https://github.com/PickNikRobotics/ros_control_boilerplate)
is used as the simulation hardware interface.

_If you do not have these packages:_

```shell
sudo apt update
sudo apt install ros-noetic-ros-control-boilerplate
sudo apt install ros-noetic-ros-controllers
```

<a id='3'></a>

## Running the Robot

The `abb_irb4600_robot` package contains a set of launch files for running
the robot. See the robot package [README.md](./abb_irb4600_robot/README.md) for usage details.
