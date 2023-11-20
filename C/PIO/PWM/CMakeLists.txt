
set(ProjectName "PIO.PWM")
set(AssemblerName "PWM")

add_executable(${ProjectName}
        main.c
        )

pico_generate_pio_header(${ProjectName}
        ${CMAKE_CURRENT_LIST_DIR}/${AssemblerName}.pio
        OUTPUT_DIR ${CMAKE_CURRENT_LIST_DIR}
        )

target_link_libraries(${ProjectName} 
        pico_stdlib
        hardware_pio
        )

#pico_enable_stdio_usb(${ProjectName} 1)
#pico_enable_stdio_uart(${ProjectName} 0)

pico_add_extra_outputs(${ProjectName})

