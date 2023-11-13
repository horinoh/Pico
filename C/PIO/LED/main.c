#include <stdio.h>

#include "pico/stdlib.h"

#include "hardware/pio.h"
#include "hardware/clocks.h"

//!< pioasm により自動生成される
#include "LED.pio.h"

//!< ピン 25 を使用している為 Pico W 非対応

int main() 
{
#ifndef PICO_DEFAULT_LED_PIN
#warning Pico W not supported
#endif

    stdio_init_all();

    //!< Pio[0, 1] それぞれに 4 つのステートマシンがある
    PIO Pio = pio0;

    //!< アセンブラプログラム (LED_program は自動生成され、LED.pio.h に定義がある)
    uint Offset = pio_add_program(Pio, &LED_program);

    //!< (使用されていない)ステートマシンを取得、無い場合エラーとする(true)
    uint Sm = pio_claim_unused_sm(Pio, true);
    
    //!< ピンは PinBase による指定値からの連番となる
    const uint PinBase = PICO_DEFAULT_LED_PIN, PinCount = 1;
    pio_gpio_init(Pio, PinBase);

    //!< ピンの入出力方向 (出力なら true)
    pio_sm_set_consecutive_pindirs(Pio, Sm, PinBase, PinCount, true);

    //!< 設定を変更する場合 (LED_program_get_default_config は自動生成され、LED.pio.h に定義がある)
    pio_sm_config Config = LED_program_get_default_config(Offset);
    {
        //!< Pico のクロックスピードは 125MHz、ステートマシンの設定で 2KHz まで落とすことが可能 [2KHz, 125MHz]
        const float Freq = 2000.0f;
        sm_config_set_clkdiv(&Config, clock_get_hz(clk_sys) / Freq);

        sm_config_set_set_pins(&Config, PinBase, PinCount);  
    }
    pio_sm_init(Pio, Sm, Offset, &Config);
    
    while (true) {
        pio_sm_set_enabled(Pio, Sm, true);
        sleep_ms(3000);
        pio_sm_set_enabled(Pio, Sm, false);
    }
}
