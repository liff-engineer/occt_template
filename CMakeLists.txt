cmake_minimum_required(VERSION 3.16)
project(occt_builder)

# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP in CMake 3.24:
if(CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
    cmake_policy(SET CMP0135 NEW)
endif()

# C++并行编译
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")
endif()

# Release版本生成调试符号
if(MSVC)
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Zi")
    set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /debug")
    set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /debug")
endif()

# 控制VS工程生成使用"文件夹"组织结构
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# 统一动态库/导入库输出位置
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$<CONFIG>)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$<CONFIG>)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$<CONFIG>)

#如果没有设置安装路径,则指定到Binary目录的publish文件夹
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/publish" CACHE PATH "default install path" FORCE)
endif()

add_subdirectory(external)
include(modules.cmake)
add_subdirectory(components)

add_subdirectory(examples)

#安装库(导入库、动态库)文件
install(DIRECTORY 
    ${CMAKE_BINARY_DIR}/$<CONFIG>/
    DESTINATION bin/$<CONFIG> 
    #FILES_MATCHING PATTERN "*.h*"
)