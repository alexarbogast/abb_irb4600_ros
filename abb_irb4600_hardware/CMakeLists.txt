cmake_minimum_required(VERSION 3.0.2)
project(abb_irb4600_hardware)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
