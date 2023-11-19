#include <stdio.h>
#include "pico/stdlib.h"

#include "hardware/sync.h"
#include "hardware/structs/ioqspi.h"

#ifndef PICO_DEFAULT_LED_PIN
#include "pico/cyw43_arch.h"
#endif

// This example blinks the Pico LED when the BOOTSEL button is pressed.
//
// Picoboard has a button attached to the flash CS pin, which the bootrom
// checks, and jumps straight to the USB bootcode if the button is pressed
// (pulling flash CS low). We can check this pin in by jumping to some code in
// SRAM (so that the XIP interface is not required), floating the flash CS
// pin, and observing whether it is pulled low.
//
// This doesn't work if others are trying to access flash at the same time,
// e.g. XIP streamer, or the other core.

//!< __no_inline_not_in_flash_func(関数) 関数をフラッシュに置かない
bool __no_inline_not_in_flash_func(GetBootselButton)() 
{
    bool ButtonState = false;

    //!< フラッシュへアクセスしないように一時的に割り込みを無効化する (割り込みハンドラがフラッシュにある可能性の為)
    uint32_t Flags = save_and_disable_interrupts(); 
    {
        const uint CS_PIN_INDEX = 1;

        //!< チップ選択を Hi-Z にする (GPIO のモードを変更してボタンの状態を読む)
        hw_write_masked(&ioqspi_hw->io[CS_PIN_INDEX].ctrl, GPIO_OVERRIDE_LOW << IO_QSPI_GPIO_QSPI_SS_CTRL_OEOVER_LSB, IO_QSPI_GPIO_QSPI_SS_CTRL_OEOVER_BITS);
        {
            //!< フラッシュ上の sleep 関数は呼び出せない
            for (volatile int i = 0; i < 1000; ++i);

            //!< SIO 内の HI GPIO レジスタでは 6 QSPI ピンの観測、制御が可能 (押されたときに Low なので注意)
            ButtonState = !(sio_hw->gpio_hi_in & (1u << CS_PIN_INDEX));
        } 
        //!< フラッシュ上のコードに戻った時におかしくならないように、GPIO のモードを戻す
        hw_write_masked(&ioqspi_hw->io[CS_PIN_INDEX].ctrl, GPIO_OVERRIDE_NORMAL << IO_QSPI_GPIO_QSPI_SS_CTRL_OEOVER_LSB, IO_QSPI_GPIO_QSPI_SS_CTRL_OEOVER_BITS);
    }
    restore_interrupts(Flags);

    return ButtonState;
}

int main() 
{
#ifdef PICO_DEFAULT_LED_PIN
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
 
    bool Prev = GetBootselButton();
    while (true) {
        bool Btn = GetBootselButton();
        if(Prev != Btn) {
            gpio_put(PICO_DEFAULT_LED_PIN, Btn);
            Prev = Btn;
        }
    }
#else
    stdio_init_all();
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }

    bool Prev = GetBootselButton();
    while (true) {
        bool Btn = GetBootselButton();
        if(Prev != Btn) {
            cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, Btn);
            Prev = Btn;
        }
    }
#endif
}
