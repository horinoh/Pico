set(ProjectName "MultiCore")
add_executable(${ProjectName}
        main.c
        )

if(${PICO_BOARD} STREQUAL pico)
        target_link_libraries(${ProjectName} 
                pico_stdlib
                # 追加
                pico_multicore
                )
elseif(${PICO_BOARD} STREQUAL pico_w)
        target_link_libraries(${ProjectName} 
                pico_stdlib
                # 追加
                pico_multicore
                pico_cyw43_arch_none
                )
else()
        message(SEND_ERROR "UNKNOWN")
endif()

pico_add_extra_outputs(${ProjectName})

