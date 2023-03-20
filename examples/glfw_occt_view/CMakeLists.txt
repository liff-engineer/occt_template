include(FetchContent)

FetchContent_Declare(
    glfw
    URL "ftp://yourhost/glfw-3.3.8.zip"
    URL_HASH SHA512=3661b74977d842e27df6f0b0ef50bdac9f34d6c9f44534af7cd357d1bcade5b3afc2e57e8a59e58f11d90966a59ff382e4faf0ca8e0825641d5f42b202df6c6d
    DOWNLOAD_NAME "glfw-3.3.8.zip"
    DOWNLOAD_DIR ${CMAKE_SOURCE_DIR}/external/downloads
)

set(GLFW_BUILD_EXAMPLES OFF)
set(GLFW_BUILD_TESTS OFF)
set(GLFW_BUILD_DOCS OFF)
set(GLFW_INSTALL OFF)
FetchContent_MakeAvailable(glfw)
set_target_properties(glfw PROPERTIES
    FOLDER  "external"  
)
set_target_properties(update_mappings PROPERTIES
    FOLDER  "external"  
)   


set(target glfw-occt)

add_executable(${target})

target_sources(${target}
    PRIVATE 
        GlfwOcctView.h
        GlfwOcctWindow.h 
        GlfwOcctView.cpp
        GlfwOcctWindow.cpp
        main.cpp     
)

# OpenGL
find_package(OpenGL REQUIRED)

target_link_libraries(${target}
    PRIVATE 
      TKVisualization  glfw
      ${OPENGL_LIBRARIES}
)
