import machine
import utime
import rp2

# set_init で ピンの初期値を設定している
# ピンはステートマシン作成時に set_base による指定値からの連番となる
@rp2.asm_pio(set_init = rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    # ピンに値をセット
    # [N] はディレイ (nop)、 Nクロック (1クロック = 500 us) 分のディレイが追加される (5 ビットなのでNの最大値は 31)
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# ステートマシンを作成 (ピン 25 は Pico W 非対応なので注意)
Sm = rp2.StateMachine(0, blink, freq = 2000, set_base = machine.Pin(25))

Sm.active(1)
utime.sleep(3)
Sm.active(0)
