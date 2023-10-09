import machine
import utime

# ADC (Analog to Digital Converter) が使えるのは GroveShield 上では A0, A1, A2
# ロータリーアングルセンサーを GroveShield の A0 へ接続しておくこと
ROTARY_ANGLE_SENSOR = machine.ADC(0)

# PWM (Pulse Width Modulation)
# LED を GroveShield の ポート18 へ接続しておくこと
LED_PWM = machine.PWM(machine.Pin(18))

#     [ ] [ ] [1] [ ] [ ]
# USB
#     [ ] [ ] [ ] [2] [ ]
#
# 1 ROTARY_ANGLE_SENSOR
# 2 LED

# 周波数
LED_PWM.freq(500)

PrevSec = 0
while True:
    # 値域は　[0, 65535] (ただし 0 にはならないので注意)
    Val = ROTARY_ANGLE_SENSOR.read_u16();
    
    # u16を引数として取るので、ロータリーアングルセンサーの値をそのまま渡せる
    LED_PWM.duty_u16(Val)

    # Year, Month, Day, Hour, Minute, Second, WeekDay, YearDay なので [5] は秒
    Sec = utime.localtime()[5]
    if PrevSec != Sec:
        PrevSec = Sec
        print("RotaryAngleSensor =", Val)
