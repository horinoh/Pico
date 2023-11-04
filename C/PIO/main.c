#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pio.h"

//!< pioasm により自動生成される
#include "addition.pio.h"

int main() 
{
    stdio_init_all();

    while (true) {
        printf("Hello, world!\n");
        sleep_ms(1000);
    }
}
