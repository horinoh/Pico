#include <stdio.h>
#include "pico/stdlib.h"

#include "hardware/pwm.h"

#define CLAMP(_val, _lhs, _rhs) MAX(MIN(_val, _rhs), _lhs)

void OnPWM()
{
    pwm_clear_irq(pwm_gpio_to_slice_num(PICO_DEFAULT_LED_PIN));

    static int Duty = 0;
    static int Direction = 1;

    Duty = CLAMP(Duty + Direction, 0, 255);
    if(255 == Duty) {
       Direction = -1; 
    }
    else if(0 == Duty) {
       Direction = 1; 
    }
    pwm_set_gpio_level(PICO_DEFAULT_LED_PIN, Duty * Duty);
}

int main() 
{
#ifdef PICO_DEFAULT_LED_PIN
    //!< PICO_DEFAULT_LED_PIN へ PWM を使うと宣言
    gpio_set_function(PICO_DEFAULT_LED_PIN, GPIO_FUNC_PWM);

    //!< スライス番号を取得
    uint Slice = pwm_gpio_to_slice_num(PICO_DEFAULT_LED_PIN);
    {
        //!< 割り込みの設定
        {
            pwm_clear_irq(Slice);
            pwm_set_irq_enabled(Slice, true);
            //!< PWM のカウンタが設定値になったときに割り込みがかかる
            irq_set_exclusive_handler(PWM_IRQ_WRAP, OnPWM);
            irq_set_enabled(PWM_IRQ_WRAP, true);
        }      

        //!< PWM スライスの設定
        {
            pwm_config Config = pwm_get_default_config();
            //!< 周波数 125 * 4 = 500 MHz
            pwm_config_set_clkdiv(&Config, 4.0f);
            pwm_init(Slice, &Config, true);
        }
    }

    while (true) {
        tight_loop_contents();
    }
#else
#endif
}
