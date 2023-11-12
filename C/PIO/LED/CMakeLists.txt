
set(ProjectName "PIO.LED")
set(AssemblerName "LED")

add_executable(${ProjectName}
        main.c
        )

# アセンブラファイル (XXX.pio) は別途作成し、ここで指定する
# ヘッダファイル (XXX.pio.h) が生成されるので、C 側でインクルードして使用する
pico_generate_pio_header(${ProjectName}
        ${CMAKE_CURRENT_LIST_DIR}/${AssemblerName}.pio
        )

# hardware_pio を追加すること
target_link_libraries(${ProjectName} 
        pico_stdlib
        hardware_pio
        )

#pico_enable_stdio_usb(${ProjectName} 1)
#pico_enable_stdio_uart(${ProjectName} 0)

pico_add_extra_outputs(${ProjectName})

