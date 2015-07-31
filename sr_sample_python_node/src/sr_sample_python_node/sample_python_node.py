#!/usr/bin/env python
"""
See README.md
"""

import rospy
from sr_sample_python_library.sample_python_class import SamplePythonClass

if __name__ == "__main__":

    rospy.init_node("sample_python_node")

    sample_object = SamplePythonClass()

    param_name = "my_python_param"
    param_value = sample_object.get_parameter_name_from_value(param_name)

    rospy.set_param(param_name, param_value)

    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rate.sleep()
