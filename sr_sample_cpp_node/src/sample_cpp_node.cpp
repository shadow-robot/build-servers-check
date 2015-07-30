#include <string>
#include "ros/ros.h"
#include "sr_sample_cpp_library/sample_cpp_class.h"

using sr_sample_cpp_library::SampleCppClass;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sample_cpp_node");
  ros::NodeHandle nh;

  SampleCppClass sample_object;

  std::string param_name("my_param");
  std::string param_value = sample_object.getParameterValueFromName(param_name);

  nh.setParam(param_name, param_value);

  ros::Rate r(5);

  while (nh.ok())
  {
    ros::spinOnce();
    r.sleep();
  }

  return 0;
}
