set(target glfw-imgui)

add_executable(${target})

target_sources(${target}
    PRIVATE 
        glfw_imgui.cpp
        ${IMGUI_SOURCE_DIR}/backends/imgui_impl_glfw.h
        ${IMGUI_SOURCE_DIR}/backends/imgui_impl_glfw.cpp   
        ${IMGUI_SOURCE_DIR}/backends/imgui_impl_opengl3.h
        ${IMGUI_SOURCE_DIR}/backends/imgui_impl_opengl3.cpp      
        ${IMGUI_SOURCE_DIR}/backends/imgui_impl_opengl3_loader.h           
)

# OpenGL
find_package(OpenGL REQUIRED)

target_link_libraries(${target}
    PRIVATE 
      glfw imgui
      ${OPENGL_LIBRARIES}
)

target_include_directories(${target}
    PRIVATE 
    ${IMGUI_SOURCE_DIR}
    ${IMGUI_SOURCE_DIR}/backends    
)