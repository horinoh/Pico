import machine
import utime

# Pulse Width Modulation (PWM) 
Pwm = machine.PWM(machine.Pin(25))
# PWM の周波数
Pwm.freq(1000)

def Clamp(Val, lhs, rhs):
    return max(lhs, min(Val, rhs))
    
Duty = 0
Direction = 1
while True:
    for _ in range(8 * 256):
        #Duty += Direction
        Duty = Clamp(Duty + Direction, 0, 255)
        if 255 == Duty:
           Direction = -1; 
        elif 0 == Duty :
           Direction = 1;
        Pwm.duty_u16(Duty * Duty)
        utime.sleep(0.001)
