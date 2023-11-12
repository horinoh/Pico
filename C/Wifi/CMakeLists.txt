set(ProjectName "Wifi")
add_executable(${ProjectName}
        main.c
        )

target_link_libraries(${ProjectName} 
        pico_stdlib
        pico_cyw43_arch_none
        #pico_cyw43_arch_lwip_poll
        #pico_cyw43_arch_lwip_threadsafe_background
        #pico_lwip_iperf
        )

# 環境変数 WIFI_SSID, WIFI_PASSWORD から 定義 WIFI_SSID, WIFI_PASSWORD を作る
target_compile_definitions(${ProjectName} PRIVATE
            WIFI_SSID=\"${WIFI_SSID}\"
            WIFI_PASSWORD=\"${WIFI_PASSWORD}\"
            )
            
pico_enable_stdio_usb(${ProjectName} 1)
pico_enable_stdio_uart(${ProjectName} 0)

pico_add_extra_outputs(${ProjectName})
