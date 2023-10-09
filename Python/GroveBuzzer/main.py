import machine
import utime

# PWM (Pulse Width Modulation)
# PASSIVE_BUZZER を GroveShield の ポート27 へ接続しておくこと
BUZZER = machine.PWM(machine.Pin(27))

#     [ ] [ ] [ ] [1] [ ]
# USB
#     [ ] [ ] [ ] [ ] [ ]
#
# 1 PASSIVE_BUZZER

Volume = 1000
# 音階関数の定義
def MusicalScale(Freq, Sec):
    BUZZER.freq(Freq)
    BUZZER.duty_u16(Volume)
    utime.sleep(Sec)
def DO(Sec):
    MusicalScale(1046, Sec)
def RE(Sec):
    MusicalScale(1175, Sec)
def MI(Sec):
    MusicalScale(1318, Sec)
def FA(Sec):
    MusicalScale(1397, Sec)
def SO(Sec):
    MusicalScale(1568, Sec)
def LA(Sec):
    MusicalScale(1768, Sec)
def SI(Sec):
    MusicalScale(1967, Sec)
def N():
    BUZZER.duty_u16(0)

for i in range(1):
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N()
    
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    
    MI(0.25)
    FA(0.25)
    SO(0.5)
    
    MI(0.25)
    FA(0.25)
    SO(0.5)
    N()
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    RE(0.25)
    SO(0.25)
    DO(0.5)
    N()
    
    RE(0.25)
    SO(0.25)
    DO(0.5)
    
N()
    
    