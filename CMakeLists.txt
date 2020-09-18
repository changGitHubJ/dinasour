project(loaddata)
cmake_minimum_required(VERSION 3.0)

set(BOOST_ROOT /opt/boost_1_67_0)

### C++11
add_compile_options(-std=c++11)

### pkgconfig (for pkg_check_modules)
find_package(PkgConfig REQUIRED)

### Python includes
pkg_check_modules(PYTHON3 python3 REQUIRED)
include_directories(${PYTHON3_INCLUDE_DIRS})

### Boost includes
include_directories(${BOOST_ROOT}/include)
link_directories(${BOOST_ROOT}/lib)

### Build
add_library(loaddata SHARED loaddata.cpp)
set_target_properties(loaddata PROPERTIES SUFFIX ".so")

target_link_libraries(loaddata boost_numpy36 boost_python36)