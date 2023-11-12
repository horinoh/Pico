import machine
import utime
import rp2

# ピン 25 を使用している為 Pico W 非対応

# Pico のクロックスピードは 125MHz、ステートマシンの設定で 2KHz まで落とすことが可能 [2KHz, 125MHz]

# asm_pio デコレータ
# 	set_init で ピンの初期値を設定している
# 	ピンはステートマシン作成時に set_base による指定値からの連番となる
@rp2.asm_pio(set_init = rp2.PIO.OUT_LOW)
def LED():
    wrap_target()
    # set(Dst, Val) Dst に Val[0, 31] をセット
    # 	[N] はディレイ (nop)、 N (最大31) クロック分のディレイが追加される
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

# ステートマシン番号、PIO x 2 それぞれに 4 つのステートマシンがあるので [0, 7]
SmNo = 0
# ステートマシンを作成(クロックを 2KHz、ピンのベースを 25)
Sm = rp2.StateMachine(SmNo, LED, freq = 2000, set_base = machine.Pin(25))

while True:
    Sm.active(1)
    utime.sleep(3)
    Sm.active(0)
    

