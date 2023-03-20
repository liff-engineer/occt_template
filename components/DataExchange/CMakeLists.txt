cmake_minimum_required(VERSION 3.16)

# 设置源码路径
set(TARGET_SOURCE_DIR "${OCCT_SOURCE_DIR}/src")

# 工程
project(TKDataExchange)

# 设置target名称
set(target TKDataExchange)

# 指定target包含的module
set(modules
    ${DataExchange}
)

# 指定target包含的package
set(packages)

foreach(module ${modules})
    foreach(package ${module})
        list(APPEND packages ${${package}})
    endforeach()
endforeach()

add_library(${target} SHARED)

target_link_libraries(${target}
    PUBLIC TKModeling TKApplication
)

# 设置预处理器定义
if(MSVC)
    target_compile_definitions(${target}
        PRIVATE UNICODE NOMINMAX
    )
endif()

include(CMakePrintHelpers)

foreach(package ${packages})
    # 设置包源码目录
    set(SOURCE_DIR "${TARGET_SOURCE_DIR}/${package}")

    # cmake_print_variables(SOURCE_DIR)

    # 提取头文件
    file(GLOB HEADER_FILES
        LIST_DIRECTORIES False
        "${SOURCE_DIR}/*.h*"
    )

    # 提取源文件
    file(GLOB SOURCE_FILES
        LIST_DIRECTORIES False
        "${SOURCE_DIR}/*.c*"
    )

    # 为VisualStudio设置源码文件夹
    source_group(
        TREE "${SOURCE_DIR}"
        PREFIX "Header Files/${package}"
        FILES ${HEADER_FILES}
    )

    source_group(
        TREE "${SOURCE_DIR}"
        PREFIX "Source Files/${package}"
        FILES ${SOURCE_FILES}
    )

    # 添加源码
    target_sources(${target}
        PRIVATE ${HEADER_FILES}
        PRIVATE ${SOURCE_FILES}
    )

    # 配置头文件路径
    target_include_directories(${target}
        PUBLIC
        "$<BUILD_INTERFACE:${SOURCE_DIR}>"
        "$<INSTALL_INTERFACE:include>"
    )

    #安装头文件
    install(DIRECTORY 
        ${SOURCE_DIR}/ 
        DESTINATION include 
        FILES_MATCHING PATTERN "*.h*"
    )    
endforeach()
