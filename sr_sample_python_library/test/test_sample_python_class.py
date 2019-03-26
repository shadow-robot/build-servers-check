#!/usr/bin/env python
# Copyright <Year> Shadow Robot Company Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
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
