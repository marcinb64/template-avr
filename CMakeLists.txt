cmake_minimum_required(VERSION 3.13)

# Project definition
project(
    Sandbox
    VERSION 0.1
    LANGUAGES CXX)

# Build customization
#set(CMAKE_BUILD_TYPE Debug)
option(WARNINGS_AS_ERRORS "Treat compiler warnings as errors" On)
option(ENABLE_SANITIZERS "Enable sanitizers" Off)
option(ENABLE_UTEST "Enable unit testing" Off)

# Helpers
include(CompilerWarnings.cmake)
include(Sanitizers.cmake)

# Project-specific settings
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)
add_sanitizers(project_options)

# Pseudo-library for adding compiler warning flags to targets
add_library(project_warnings INTERFACE)
set_project_warnings(project_warnings)

# Misc options
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (ENABLE_UTEST)
    include(CTest)
endif ()

# Project structure
add_subdirectory(app)
add_subdirectory(somelib)
add_subdirectory(core)
