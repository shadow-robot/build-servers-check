cmake_minimum_required(VERSION 2.8.3)
project(sr_sample_cpp_node)

find_package(catkin REQUIRED COMPONENTS
  roscpp
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES sr-sample-cpp-node
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)

add_executable(sample_cpp_node src/sample_cpp_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
# add_dependencies(sr-sample-cpp-node_node sr-sample-cpp-node_generate_messages_cpp)

target_link_libraries(sample_cpp_node
  ${catkin_LIBRARIES}
)

#############
## Install ##
#############

install(TARGETS sample_cpp_node
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest_gtest(test_sample_cpp_node test/test_sample_cpp_node.test test/test_sample_cpp_node.cpp)
  target_link_libraries(test_sample_cpp_node ${catkin_LIBRARIES})
endif()
