import machine
import utime

# ボタンを GroveShield の 16 ポートへ接続しておくこと
BUTTON = machine.Pin(16, machine.Pin.IN)
# LED を GroveShield の 18 ポートへ接続しておくこと
LED = machine.Pin(18, machine.Pin.OUT)

#     [ ] [ ] [ ] [ ] [ ]
# USB
#     [ ] [ ] [1] [2] [ ]
#
# 1 BUTTON
# 2 LED

# 3 回点滅
for i in range(3):   
    LED.value(1)
    utime.sleep(1)
    print("Loop =", i, "LED =", LED.value())
    
    LED.value(0)
    utime.sleep(1)
    print("Loop =", i, "LED =", LED.value())
print("Loop End")

# ボタンを押したら点灯
Prev = 0
while True:
    Btn = BUTTON.value()
    if Prev != Btn:
        LED.value(Btn)
        print("Button =", Btn, "LED =", LED.value())
    Prev = Btn


        