cmake_minimum_required(VERSION 3.16)

# 设置源码路径
set(TARGET_SOURCE_DIR "${OCCT_SOURCE_DIR}/src")

# 工程
project(TKVisualization)

# 设置target名称
set(target TKVisualization)

# 指定target包含的module
set(modules
    ${Visualization}
)

# 移除 TKIVtk 以避免编译问题
list(REMOVE_ITEM modules TKIVtk)
list(REMOVE_ITEM modules TKOpenGles)
list(REMOVE_ITEM modules TKOpenGlesTest)

# 指定target包含的package
set(packages)

foreach(module ${modules})
    foreach(package ${module})
        list(APPEND packages ${${package}})
    endforeach()
endforeach()

# 配置FreeType、FreeImage、FFmpeg
add_definitions(-DHAVE_FREETYPE)
add_definitions(-DHAVE_FREEIMAGE)
add_definitions(-DHAVE_OPENGL_EXT)
add_definitions(-DHAVE_D3D)

add_library(${target} SHARED)

find_package(OpenGL REQUIRED)
target_include_directories(${target}
    PRIVATE ${OPENGL_INCLUDE_DIRS}
    ${FREEIMAGE_SOURCE_DIR}/include
    ${FREETYPE_SOURCE_DIR}/include
)

target_link_directories(${target}
    PRIVATE ${FREEIMAGE_SOURCE_DIR}/lib
)

target_link_libraries(${target}
    PUBLIC TKModeling
    PRIVATE ${OPENGL_LIBRARIES} Winmm.lib
    ${FREETYPE_SOURCE_DIR}/lib/freetype.lib
)

#部署依赖的动态库 
add_custom_command(TARGET ${target} POST_BUILD 
    COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${FREETYPE_SOURCE_DIR}/bin/freetype.dll $<TARGET_FILE_DIR:${target}>/
    COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${FREEIMAGE_SOURCE_DIR}/bin/FreeImage.dll $<TARGET_FILE_DIR:${target}>/    
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