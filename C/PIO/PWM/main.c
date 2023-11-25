#include <stdio.h>

#include "pico/stdlib.h"

#include "hardware/pio.h"
#include "hardware/clocks.h"

#include "PWM.pio.h"

void SetPeriod(const PIO Pio, const uint Sm, const uint32_t Period) 
{
    pio_sm_set_enabled(Pio, Sm, false);{
        pio_sm_put_blocking(Pio, Sm, Period);
        
        //!< アセンブラ命令を発行 (ISR に「期間」を保持)
        {
            //!< "pull" に相当
            pio_sm_exec(Pio, Sm, pio_encode_pull(false, false));
            //!< "out isr, 32" に相当 
            pio_sm_exec(Pio, Sm, pio_encode_out(pio_isr, 32));
        }
    } pio_sm_set_enabled(Pio, Sm, true);
}

int main() 
{
    //!< ピン 25 を使用している為 Pico W 非対応
#ifndef PICO_DEFAULT_LED_PIN
#warning Pico W not supported
#else
    stdio_init_all();

    PIO Pio = pio0;

    uint Offset = pio_add_program(Pio, &PWM_program);

    uint Sm = pio_claim_unused_sm(Pio, true);
    
    const uint SideSetPinBase = PICO_DEFAULT_LED_PIN, SideSetPinCount = 1;
    pio_gpio_init(Pio, SideSetPinBase);

    pio_sm_config Config = PWM_program_get_default_config(Offset);
    {
        sm_config_set_clkdiv(&Config, 1);

        //!< sideset ピン (個数はアセンブラ内で指定する .side_set N)
        sm_config_set_sideset_pins(&Config, SideSetPinBase);

        pio_sm_set_consecutive_pindirs(Pio, Sm, SideSetPinBase, SideSetPinCount, true);
    }
    pio_sm_init(Pio, Sm, Offset, &Config);
    
    SetPeriod(Pio, Sm, (1u << 16) - 1);
    int Level = 0;
    while (true) {
        //printf("Level = %d\n", Level);
        pio_sm_put_blocking(Pio, Sm, Level * Level);
        Level = ++Level % 256;
        sleep_ms(10);
    }
#endif
}
