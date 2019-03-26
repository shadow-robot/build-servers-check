#!/usr/bin/env python
# Copyright 2019 Shadow Robot Company Ltd.
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
