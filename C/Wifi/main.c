#include <stdio.h>
#include "pico/stdlib.h"

#ifndef PICO_DEFAULT_LED_PIN
#include "pico/cyw43_arch.h"
#endif

int main() 
{
#ifndef PICO_DEFAULT_LED_PIN
    stdio_init_all();
    
    if (cyw43_arch_init()) {
       printf("failed to initialise\n");
       return 1;
    }
    
    while (true) {
        printf("Hello, world!\n");
        sleep_ms(1000);
    }
#else
#endif
}
