#!/usr/bin/env python
"""
See README.md
"""
import rospy
from sr_benchmarking_msgs.srv import ExecuteBenchmarking, ExecuteBenchmarkingResponse
import time


def execute_benchmarking(request):

    start = time.time()
    while not rospy.is_shutdown():
        param_value = rospy.get_param('my_python_param')
        if 'my_python_param_test' != param_value:
            rospy.sleep(0.1)
        else:
            break

    end = time.time()
    time_spend = end - start

    with open(request.output_file, 'a') as file:
        file.write('result,' + str(time_spend))
    return ExecuteBenchmarkingResponse(True)

if __name__ == "__main__":

    rospy.init_node('sample_node_benchmarking')
    _ = rospy.Service('execute_benchmarking', ExecuteBenchmarking, execute_benchmarking)
    rospy.spin()
