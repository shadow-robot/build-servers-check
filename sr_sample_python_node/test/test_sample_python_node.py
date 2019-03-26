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
