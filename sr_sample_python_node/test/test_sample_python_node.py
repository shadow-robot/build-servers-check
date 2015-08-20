#!/usr/bin/env python
"""
See README.md
"""

import rospy
from unittest import TestCase


class TestSamplePythonNode(TestCase):

    def test_parameter_name(self):

        rospy.init_node("test_sample_python_node")

        rate = rospy.Rate(2)
        rate.sleep()

        param_value = rospy.get_param("my_python_param")
        expected_value = "my_python_param_test"

        self.assertEqual(expected_value, param_value)

if __name__ == '__main__':
    import rostest

    rostest.rosrun('sr_sample_python_library', 'test_sample_python_node',
                   TestSamplePythonNode)
