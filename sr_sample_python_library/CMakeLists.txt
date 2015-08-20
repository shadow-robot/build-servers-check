cmake_minimum_required(VERSION 2.8.3)
project(sr_sample_python_library)

find_package(catkin REQUIRED)

catkin_python_setup()

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS rospy
)

#############
## Install ##
#############

install(PROGRAMS
  src/${PROJECT_NAME}/sample_python_class.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############

catkin_add_nosetests(test)
