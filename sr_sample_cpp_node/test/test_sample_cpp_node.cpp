#include <gtest/gtest.h>
#include "ros/ros.h"

TEST(SampleCppTestSuite, checkParameterValue)
{
    // TODO: Add code to read parameter from server
    ASSERT_TRUE(true);
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
