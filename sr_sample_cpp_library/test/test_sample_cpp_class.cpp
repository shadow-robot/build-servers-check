#include <gtest/gtest.h>
#include <string>

#include "sr_sample_cpp_library/sample_cpp_class.h"

using sr_sample_cpp_library::SampleCppClass;

TEST(SampleCppClassTestSuite, checkGetParameterValueFromName)
{
    SampleCppClass sample_object;

    std::string param1("my_param_one");
    std::string param2("my_param_two");

    std::string expected_result1("my_param_one_test");
    std::string expected_result2("my_param_two_test");

    EXPECT_EQ(expected_result1, sample_object.getParameterValueFromName(param1));
    EXPECT_EQ(expected_result2, sample_object.getParameterValueFromName(param2));
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
