import machine
import utime
import rp2

@rp2.asm_pio(sideset_init = rp2.PIO.OUT_LOW)
def PWM():
    # FIFO から OSR へ、ノンブロッキングなので FIFO に無い場合は X の値が OSR へコピーされる、サイドセットは 0
    pull(noblock) .side(0)
    # X には最新の OSR 値、もしくは前回の X の値そのままになる (FIFO から取得できたかどうかによる)
    mov(x, osr)
    # ISR には「期間」が入っている、Y はカウンタとして使用 (ここでは入力として ISR を使用していないので、「期間」を保持する領域として活用している)
    mov(y, isr)
    label("loop")
    # X == Y の時以外は何もしない
    jmp(x_not_y, "skip")
    # X == Y となったらここに来る サイドセットを 1
    nop()         .side(1)
    label("skip")
    # 「期間」カウンタ Y が 0 になるまでループ
    jmp(y_dec, "loop")

class PIOPWM:
    def __init__(self, SmNo, Period):
        self.Sm = rp2.StateMachine(SmNo, PWM, freq = -1, sideset_base = machine.Pin(25))
        # アセンブラ命令を発行 (ISR に「期間」を保持)
        self.Sm.active(0)
        self.Sm.put(Period)
        self.Sm.exec("pull()")
        self.Sm.exec("out(isr, 32)")
        self.Sm.active(1)

    def SetLevel(self, value):
        self.Sm.put(value)

Pwm = PIOPWM(0, Period = (1 << 16) - 1)
Level = 0
while True:
    #print("Level = ", Level);
    Pwm.SetLevel(Level ** 2)
    Level = (Level + 1) % 256;
    utime.sleep_ms(10)
        
