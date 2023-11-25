#include <stdio.h>
#include <ctype.h>
#include "pico/stdlib.h"

#ifndef PICO_DEFAULT_LED_PIN
#include "pico/cyw43_arch.h"
#endif

const uint DOT_PERIOD_MS = 100;
//!< モールスのパターン
const char *MorseLetters[] = {
        ".-",    // A
        "-...",  // B
        "-.-.",  // C
        "-..",   // D
        ".",     // E
        "..-.",  // F
        "--.",   // G
        "....",  // H
        "..",    // I
        ".---",  // J
        "-.-",   // K
        ".-..",  // L
        "--",    // M
        "-.",    // N
        "---",   // O
        ".--.",  // P
        "--.-",  // Q
        ".-.",   // R
        "...",   // S
        "-",     // T
        "..-",   // U
        "...-",  // V
        ".--",   // W
        "-..-",  // X
        "-.--",  // Y
        "--.."   // Z
};
//!< モールスのパターンを LED 出力
void PutMorse(const char *Pattern) 
{
    for (; *Pattern; ++Pattern) {
#ifdef PICO_DEFAULT_LED_PIN
        gpio_put(PICO_DEFAULT_LED_PIN, 1);
#else
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
#endif
        
        sleep_ms(DOT_PERIOD_MS * (*Pattern == '.' ? 1 : 3));

#ifdef PICO_DEFAULT_LED_PIN
        gpio_put(PICO_DEFAULT_LED_PIN, 0);
#else
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
#endif

        sleep_ms(DOT_PERIOD_MS * 1);
    }
    sleep_ms(DOT_PERIOD_MS * 2);
}
//!< 文字列をモールスとして LED 出力
void ToMorse(const char *Str) 
{
    for (; *Str; ++Str) {
        if(isalpha(*Str)) {
            const char *Pattern = MorseLetters[tolower(*Str) - 'a'];
            PutMorse(Pattern);
            printf("%s == %s\n", *Str, Pattern);
        } else if (isspace(*Str)) {
            sleep_ms(DOT_PERIOD_MS * 4);
            puts(" \n");
        } 
    }
}

int main()
{
#ifdef PICO_DEFAULT_LED_PIN
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
 
    ToMorse("Hello World");
    while (true) {
        gpio_put(PICO_DEFAULT_LED_PIN, 1);
        sleep_ms(250);
        gpio_put(PICO_DEFAULT_LED_PIN, 0);
        sleep_ms(250);
    }
#else
    stdio_init_all();
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }

    ToMorse("Hello World");
    while (true) {
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
        sleep_ms(250);
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
        sleep_ms(250);
    }
#endif
}
