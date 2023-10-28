
set(ProjectName "Temperature")
add_executable(${ProjectName}
        main.c
        )

target_link_libraries(${ProjectName} 
        pico_stdlib
        hardware_adc
        )

pico_enable_stdio_usb(${ProjectName} 1)
pico_enable_stdio_uart(${ProjectName} 0)

pico_add_extra_outputs(${ProjectName})

#example_auto_set_url(${ProjectName})
