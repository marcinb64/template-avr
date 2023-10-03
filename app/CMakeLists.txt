set(MODULE_ID sandbox)

add_executable(${MODULE_ID} 
    main.cpp)

target_compile_definitions(${MODULE_ID} PUBLIC F_CPU=${F_CPU})

target_link_libraries(${MODULE_ID} 
    PRIVATE 
        project_warnings 
        project_options
        core)

# Pass conan lib includes as -I rather than -isystem.
# -isystem includes are force-treated as extern "C"
# https://github.com/conan-io/conan/issues/269
set_target_properties(${MODULE_ID}
    PROPERTIES
    NO_SYSTEM_FROM_IMPORTED ON)
