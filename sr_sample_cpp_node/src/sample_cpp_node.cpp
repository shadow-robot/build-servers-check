#include "ros/ros.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sample_cpp_node");
  ros::NodeHandle nh;

  nh.setParam("my_param", "hello world");

  ros::Rate r(5);

  while (nh.ok())
  {
    ros::spinOnce();
    r.sleep();
  }

  return 0;
}
