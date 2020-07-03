| Build server  | Status |
|---------------|--------|
| Travis | [![Build Status](https://travis-ci.org/shadow-robot/build-servers-check.svg)](https://travis-ci.org/shadow-robot/build-servers-check) |
| Shippable | [![Build Status](https://api.shippable.com/projects/55ba073fedd7f2c0528ca1a8/badge?branchName=indigo-devel)](https://app.shippable.com/projects/55ba073fedd7f2c0528ca1a8/builds/latest) |
| Semaphore | [![Build Status](https://semaphoreci.com/api/v1/projects/3d9a5e21-cb5b-4fae-a942-93e6515682cb/571657/shields_badge.svg)](https://semaphoreci.com/shadow-robot/build-servers-check) |
| Circle | [![Circle CI](https://circleci.com/gh/shadow-robot/build-servers-check.svg?style=shield)](https://circleci.com/gh/shadow-robot/build-servers-check)

Check | Status
---|---
Build|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoicGtqdWh6TzhLTXVObHZpTlhoUThMTW9PcEU5NEtaSU5ZbXo2elk0V2ppWkI0eGhGU2tpZXpDYVRKVXdGN2E4Ykc2MlBFOWcyUVI3YkNxVFpabERvZnRzPSIsIml2UGFyYW1ldGVyU3BlYyI6InkxM3J1b1NURzJpeXY4S24iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=kinetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_build-servers-check_kinetic-devel_install_check/)
Style|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWGJmVXU2S01pVm1xMzZIRVYzaEdTbUQ1b3VCckRqUU5ra284MDZHZHpzc3NnTFh2RlMrRWEySmdLQ1BOczVEYmpWeGpxeXBpRDl6TGZ3SGdESW02UmJZPSIsIml2UGFyYW1ldGVyU3BlYyI6InVYTHE5VXhWc3loR0dKYlQiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=kinetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_build-servers-check_kinetic-devel_style_check/)
Code Coverage|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiVHRzcDBqV2Z4bnJZWjUxcFBQalhLYmlpOGtheTk5NGVIeDFHQXE1bHlOakJGV3lJak5PRXhydVo4QmlxclNMMThqVU9tQ0tXRmRIUUtpT3lFT0xMbzhzPSIsIml2UGFyYW1ldGVyU3BlYyI6IkRFQzlaZStXVWNSVnNYRXYiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=kinetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_build-servers-check_kinetic-devel_code_coverage/)


# build-servers-check

The sample stack to check status of the build servers.

This stack contains four packages

 * **sr_sample_cpp_library** - sample C++ library package with one class and unit test
 * **sr_sample_cpp_node** - C++ node which depend on C++ library and integration test 
 * **sr_sample_python_library** - sample Python library with one class and unit test
 * **sr_sample_python_node** - Python node which depend on Python library and integration test
  
Every supported CI server runs all major modules on this sample stack in order to check if modules are working on the server.
