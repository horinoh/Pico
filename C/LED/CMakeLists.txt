set(ProjectName "LED")
add_executable(${ProjectName}
        main.c
        )

if(${PICO_BOARD} STREQUAL pico)
        # PICO_BOARD == pico の場合
        target_link_libraries(${ProjectName} 
                pico_stdlib
                )
elseif(${PICO_BOARD} STREQUAL pico_w)
        # PICO_BOARD == pico_w の場合
        target_link_libraries(${ProjectName} 
                pico_stdlib
                # Pico W では pico_cyw43_arch_none が必要
                pico_cyw43_arch_none
                )
else()
        message(SEND_ERROR "UNKNOWN")
endif()

pico_add_extra_outputs(${ProjectName})

