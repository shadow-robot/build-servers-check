| Build server  | Status |
|---------------|--------|
| AWS | ![Build Status](https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUXc2R0VLRnhQNTRnN0pTRmFLVkUwMUVxTmxENERvOHhvSDF4RXRFTE1zQlpYOUxhUzFESWJJcDllNWFuOVRwdU4zY1MwZHptVTNHSk1IMzAxVDN3Z1NjPSIsIml2UGFyYW1ldGVyU3BlYyI6ImtlTVpRUVYyWi9mRnBYcDQiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=kinetic-devel) 
| Travis | [![Build Status](https://travis-ci.org/shadow-robot/build-servers-check.svg)](https://travis-ci.org/shadow-robot/build-servers-check) |
| Shippable | [![Build Status](https://api.shippable.com/projects/55ba073fedd7f2c0528ca1a8/badge?branchName=kinetic-devel)](https://app.shippable.com/projects/55ba073fedd7f2c0528ca1a8/builds/latest) |
| Semaphore | [![Build Status](https://semaphoreci.com/api/v1/projects/3d9a5e21-cb5b-4fae-a942-93e6515682cb/571657/shields_badge.svg)](https://semaphoreci.com/shadow-robot/build-servers-check) |
| Circle | [![Circle CI](https://circleci.com/gh/shadow-robot/build-servers-check.svg?style=shield)](https://circleci.com/gh/shadow-robot/build-servers-check) |
| CodeCov | [![codecov.io](http://codecov.io/github/shadow-robot/build-servers-check/coverage.svg?branch=kinetic-devel)](http://codecov.io/github/shadow-robot/build-servers-check?branch=kinetic-devel) |
    
# build-servers-check

The sample stack to check status of the build servers.

This stack contains four packages

 * **sr_sample_cpp_library** - sample C++ library package with one class and unit test
 * **sr_sample_cpp_node** - C++ node which depend on C++ library and integration test 
 * **sr_sample_python_library** - sample Python library with one class and unit test
 * **sr_sample_python_node** - Python node which depend on Python library and integration test
  
Every supported CI server runs all major modules on this sample stack in order to check if modules are working on the server.
 
