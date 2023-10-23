import machine
import utime

# Pulse Width Modulation(PWM) のパルス幅がサーボの回転角を決定する
# 角度   パルス幅 u16表記
#   0    0.61ms    4000
#  45     1.1ms    7250
#  90     1.6ms   10500
# 180s    2.6ms   17000
#
# よって以下の計算式になる
# Ang / 180 * 13000 + 40000

#     [ ] [ ] [ ] [ ] [ ]
# USB
#     [ ] [ ] [ ] [2] [1]
#
# 1 SERVO
# 2 MOTION_SENSOR

class SERVO:
    def __init__(self, Pin):
        self.PWM = machine.PWM(Pin)
    
    def Turn(self, Val):
        self.PWM.freq(100)
        self.PWM.duty_u16(int(Val / 180 * 13000 + 4000))

Servo = SERVO(machine.Pin(20))
MotSensor = machine.Pin(18, machine.Pin.IN)

while True:
    if MotSensor.value() == 0:
        continue
    
    print("MotSensor = ", MotSensor.value())
    
    Servo.Turn(160)
    utime.sleep(2)

    Servo.Turn(20)
    utime.sleep(2)

