cmake_minimum_required(VERSION 2.8.3)
project(sr_sample_python_node)

find_package(catkin REQUIRED)

find_package(sr_sample_python_library REQUIRED)

catkin_python_setup()


###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS sr_sample_python_library
)

#############
## Install ##
#############

install(PROGRAMS
  src/${PROJECT_NAME}/sample_python_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############

if (CATKIN_ENABLE_TESTING)

  find_package(rostest REQUIRED)
  add_rostest(test/test_sample_python_node.test)

endif()
