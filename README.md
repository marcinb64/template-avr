# Project name

## TODO

 - [ ] [Choose license](https://choosealicense.com) and update LICENSE file
 - [ ] Update project metadata in conanfile.py
 - [ ] Update project name in CMakeLists.txt
 - [ ] Update this README file
 - [ ] Customize .clang-tidy and .clang-format as needed

## About

## Dependencies

Example dependencies

 * Catch2 for unit testing

## Build

Example build commands for AVR 2560 (Arduino Mega). Assumes a Conan profile named `avr-mega2560` exists.

    conan install conanfile.py --build=missing -pr:b=default -pr:h=avr-mega2560
    source build/Release/generators/conanbuild.sh   # Load cross-compile config
    cmake --preset conan-avr-release -DF_CPU=16000000 
    cmake --build build/Release

    # Build the library
    conan create . --profile=avr-mega2560

Example build commands for running unit tests on Linux. Assumes a Conan profile named `linux-debug` exists.

    conan install conanfile.py --build=missing --profile=linux-debug -o platform=linux
    cmake --preset conan-linux-debug -DENABLE_UTEST=On -DENABLE_SANITIZERS=On
    cmake --build build/Debug --target utest_core --target utest_somelib

    ./build/Debug/core/utest_core 
    ./build/Debug/somelib/utest_somelib 

Example conan profile: `avr-mega2560`

    [settings]
    arch=avr
    build_type=Release
    compiler=gcc
    compiler.cppstd=gnu17
    compiler.libcxx=libstdc++11
    compiler.version=7
    os=baremetal

    [conf]
    tools.build:cflags=["-mmcu=atmega2560"]
    tools.build:cxxflags=["-mmcu=atmega2560"]

    [buildenv]
    CHOST=avr
    CONAN_CMAKE_FIND_ROOT=/opt/avr8-gnu-toolchain-linux_x86_64
    AR=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-ar
    AS=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-as
    RANLIB=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-ranlib
    CC=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-gcc
    CXX=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-g++
    STRIP=/opt/avr8-gnu-toolchain-linux_x86_64/bin/avr-strip

Example conan profile: `linux-debug`

    [settings]
    arch=x86_64
    build_type=Debug
    compiler=gcc
    compiler.cppstd=20
    compiler.libcxx=libstdc++11
    compiler.version=12
    os=Linux
