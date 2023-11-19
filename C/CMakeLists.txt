cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

set(Folder "C")
project(${Folder} C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_subdirectory(Hello)
add_subdirectory(LED)
add_subdirectory(Button)
add_subdirectory(Temperature)
add_subdirectory(Wifi)
add_subdirectory(PIO)
