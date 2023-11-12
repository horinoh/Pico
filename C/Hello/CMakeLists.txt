set(ProjectName "Hello")
add_executable(${ProjectName}
        main.c
        )

# pull in common dependencies
target_link_libraries(${ProjectName} 
        pico_stdlib
        )

# USB CDC(USBシリアル) 軽油での出力を有効化
pico_enable_stdio_usb(${ProjectName} 1)
# UART 経由での出力を無効化
pico_enable_stdio_uart(${ProjectName} 0)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(${ProjectName})
