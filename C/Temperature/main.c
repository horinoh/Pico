#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"

//!< # u16 [0, 65535] を 電圧 [0, 3.3] へ変換する
float ToVoltage(const int i)
{
    return (float)i * (3.3f / (1 << 12));
}

//!< 電圧を摂氏へ変換する
float ToCelsius(const float Voltage)
{
    //!< Pico RP2040 データシートより、電圧値を摂氏へ変換するのは以下の式となる
    return 27.0f - (Voltage - 0.706f) / 0.001721f;
} 

int main()
{
    stdio_init_all();

    //!< RP2040 には温度センサーが内蔵されている
    adc_init();
    adc_set_temp_sensor_enabled(true);
    adc_select_input(4);

    while (true) {
        const float Celsius = ToCelsius(ToVoltage(adc_read()));
        printf("%2.2f\n", Celsius);
        sleep_ms(1000);
    }
}
