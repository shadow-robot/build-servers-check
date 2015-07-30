#include <gtest/gtest.h>
#include "ros/ros.h"

TEST(SampleCppTestSuite, checkParameterValue)
{
  const ros::M_string remapping_args;
  ros::init(remapping_args, "sample_cpp_node");
  const ros::NodeHandle nh;

  ros::Rate rate(2);
  ros::spinOnce();
  rate.sleep();

  std::string param_value;
  const bool result = nh.getParam("my_param", param_value);
  const std::string expected_value("my_param_test");

  ASSERT_TRUE(result);
  ASSERT_EQ(expected_value, param_value);
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
