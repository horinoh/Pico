#include <stdio.h>

#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"

//!< pioasm により自動生成される
#include "LED.pio.h"

//!< ピン 25 を使用している為 Pico W 非対応

//!< Pico のクロックスピードは 125MHz、ステートマシンの設定で 2KHz まで落とすことが可能 [2KHz, 125MHz]

int main() 
{
    stdio_init_all();

    //!< Pio[0, 1] それぞれに 4 つのステートマシンがある
    PIO Pio = pio0;

    //!< アセンブラプログラム (LED_program は自動生成され、LED.pio.h に定義がある)
    uint Offset = pio_add_program(Pio, &LED_program);

    //!< (使用されていない)ステートマシンを取得、無い場合エラーとする(true)
    uint Sm = pio_claim_unused_sm(Pio, true);
    
#if false
    //!< デフォルト設定 (LED_program_init は自動生成され、LED.pio.h に定義がある)
    LED_program_init(Pio, Sm, Offset);
#else
    //!< 設定を変更する場合 (LED_program_get_default_config は自動生成され、LED.pio.h に定義がある)
    pio_sm_config Config = LED_program_get_default_config(Offset);
    {
        //!< Pico のクロックスピードは 125MHz、ステートマシンの設定で 2KHz まで落とすことが可能 [2KHz, 125MHz]
        const float Freq = 1.0f;//2000.0f;
        sm_config_set_clkdiv(&Config, clock_get_hz(clk_sys) / Freq);

        //!< ピンは PinBase による指定値からの連番となる
        const uint PinBase = 25;
        sm_config_set_in_pins(&Config, PinBase);
    }
    pio_sm_init(Pio, Sm, Offset, &Config);
#endif
    
    while (true) {
        pio_sm_set_enabled(Pio, Sm, true);
        sleep_ms(3000);
        pio_sm_set_enabled(Pio, Sm, false);
    }
}
