#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

int main() 
{
    stdio_init_all();
    
    if (cyw43_arch_init()) {
       printf("failed to initialise\n");
       return 1;
    }
    
    while (true) {
        printf("Hello, world!\n");
        sleep_ms(1000);
    }
}
