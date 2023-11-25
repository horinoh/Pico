#include <stdio.h>
#include "pico/stdlib.h"

#include "pico/multicore.h"

#ifndef PICO_DEFAULT_LED_PIN
#include "pico/cyw43_arch.h"
#endif

void OnCore1() 
{
    // multicore_fifo_push_blocking(FLAG_VALUE);

    // uint32_t g = multicore_fifo_pop_blocking();

    // if (g != FLAG_VALUE)
    //     printf("Hmm, that's not right on core 1!\n");
    // else
    //     printf("Its all gone well on core 1!");

#ifdef PICO_DEFAULT_LED_PIN
    gpio_put(PICO_DEFAULT_LED_PIN, 1);
#else
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
#endif

    printf("OnCore1");

    // while (1) {
    //     tight_loop_contents();
    // }
}

int main() 
{
#ifdef PICO_DEFAULT_LED_PIN
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
#else
    stdio_init_all();
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }
#endif

    multicore_launch_core1(OnCore1);
}
