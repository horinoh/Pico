
set(ProjectName "LED")
add_executable(${ProjectName}
        main.c
        )

target_link_libraries(${ProjectName} 
        pico_stdlib
        pico_cyw43_arch_none # Pico W系 では必要
        )

pico_add_extra_outputs(${ProjectName})

#example_auto_set_url(${ProjectName})
