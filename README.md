# build-servers-check

Shippable

[![Build Status](https://api.shippable.com/projects/55ba073fedd7f2c0528ca1a8/badge?branchName=indigo-devel)](https://app.shippable.com/projects/55ba073fedd7f2c0528ca1a8/builds/latest)

Semaphore

[![Build Status](https://semaphoreci.com/api/v1/projects/2a789441-5243-43ab-99e5-2efa81d725da/516315/shields_badge.svg)](https://semaphoreci.com/andriy/build-servers-check)

Circle

[![Circle CI](https://circleci.com/gh/shadow-robot/build-servers-check.svg?style=shield)](https://circleci.com/gh/shadow-robot/build-servers-check)

CodeCov

[![codecov.io](http://codecov.io/github/shadow-robot/build-servers-check/coverage.svg?branch=indigo-devel)](http://codecov.io/github/shadow-robot/build-servers-check?branch=indigo-devel)


Shadow's Jenkins

[![Build Status](http://jenkins.shadow.local:8080/buildStatus/icon?job=auto_build-servers-check_indigo-devel_unit_tests_and_code_coverage)](http://jenkins.shadow.local:8080/job/auto_build-servers-check_indigo-devel_unit_tests_and_code_coverage)

The sample stack to check status of the build servers.

This stack contains four packages

 * **sr_sample_cpp_library** - sample C++ library package with one class and unit test
 * **sr_sample_cpp_node** - C++ node which depend on C++ library and integration test 
 * **sr_sample_python_library** - sample Python library with one class and unit test
 * **sr_sample_python_node** - Python node which depend on Python library and integration test
  
Every supported CI server runs all major modules on this sample stack in order to check if modules are working on the server.


