#!/usr/bin/env python
"""
See README.md
"""

from unittest import TestCase
from sr_sample_python_library.sample_python_class import SamplePythonClass


class TestSamplePythonClass(TestCase):

    def test_get_parameter_name_from_value(self):

        my_convertor = SamplePythonClass()

        param1 = "my_python_param_1"
        param2 = "my_python_param_2"

        expected_value1 = "my_python_param_1_test"
        expected_value2 = "my_python_param_2_test"

        self.assertEqual(expected_value1,
                         my_convertor.get_parameter_name_from_value(param1))

        self.assertEqual(expected_value2,
                         my_convertor.get_parameter_name_from_value(param2))

if __name__ == '__main__':
    import rosunit

    rosunit.rosrun('sr_sample_python_library', 'test_sample_python_class',
                   TestSamplePythonClass)
