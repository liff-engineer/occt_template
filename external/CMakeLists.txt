include(FetchContent)
include(CMakePrintHelpers)

FetchContent_Declare(
    freeimage
    URL https://dev.opencascade.org/system/files/occt/3rdparty/freeimage-3.17.0-vc14-64.zip
    URL_HASH SHA512=9eb52b854e90d9051b5e931e35d3284d3b11ffea48499efa63535fb2c7527606ccb089eaf98018ac7b66f936f98abf9686d71e513ee9ef4db8678184bf48ef0c
    DOWNLOAD_NAME "freeimage-3.17.0-vc14-64.zip"
    DOWNLOAD_DIR ${CMAKE_SOURCE_DIR}/external/downloads
)

FetchContent_Declare(
    freetype
    URL https://dev.opencascade.org/system/files/occt/3rdparty/freetype-2.5.5-vc14-64.zip
    URL_HASH SHA512=562d9b738254575a3e9f04400ea60c6f74865d907e8c445cc4fd470ea121198cdf2a90d9aab043c4ae0a650ab5c8cc6208b0577cd3ce8536359a48b4c0abf597
    DOWNLOAD_NAME "freetype-2.5.5-vc14-64.zip"
    DOWNLOAD_DIR ${CMAKE_SOURCE_DIR}/external/downloads
)

FetchContent_Declare(
    occt
    URL https://github.com/Open-Cascade-SAS/OCCT/archive/refs/tags/V7_6_3.tar.gz
    URL_HASH SHA512=bdcdc79ce5bf1df4d7a4b90a4ce33fabf5fefeb75f33d58c571014c5cff9e4e2d444a518b741002654e29f0b50babad852b10636c3c888afb49628e1752abca7
    DOWNLOAD_NAME "OCCT-7_6_3.tar.gz"
    DOWNLOAD_DIR ${CMAKE_SOURCE_DIR}/external/downloads
)

FetchContent_GetProperties(freeimage)

if(NOT freeimage_POPULATED)
    FetchContent_Populate(freeimage)

    set(FREEIMAGE_SOURCE_DIR ${freeimage_SOURCE_DIR} CACHE INTERNAL "freeimage source directory")
endif()

FetchContent_GetProperties(freetype)

if(NOT freetype_POPULATED)
    FetchContent_Populate(freetype)

    set(FREETYPE_SOURCE_DIR ${freetype_SOURCE_DIR} CACHE INTERNAL "freetype source directory")
endif()

FetchContent_GetProperties(occt)

if(NOT occt_POPULATED)
    FetchContent_Populate(occt)

    set(OCCT_SOURCE_DIR ${occt_SOURCE_DIR} CACHE INTERNAL "occt source directory")
endif()