from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class ExampleRecipe(ConanFile):
    name = "example"
    version = "0.0.1"

    # Optional metadata
    license = "Unlicense"
    author = "someone@somesite.com"
    #url = "http://somesite.com"
    description = "Some lib"
    topics = ("avr")

    # Binary configuration
    settings = "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "platform": ["avr", "linux"]}
    default_options = {"shared": False, "fPIC": False, "platform": "avr"}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "*.cmake", "app/*", "somelib/*", "core/*"
    generators = "CMakeDeps"

    def requirements(self):
        if (self.options.platform == 'linux'):
            self.requires("catch2/3.1.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.presets_prefix = "conan-" + str(self.options.platform)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build(target="somelib")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["somelib"]
