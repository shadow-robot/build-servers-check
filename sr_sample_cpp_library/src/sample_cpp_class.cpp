#include "sr_sample_cpp_library/sample_cpp_class.h"

#include <string>

namespace sr_sample_cpp_library
{

std::string SampleCppClass::getParameterValueFromName(const std::string &parameter_name) const
{
    std::string result = parameter_name;
    result.append("_test");
    return result;
}

}
