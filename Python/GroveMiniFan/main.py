import machine

BUTTON = machine.Pin(16, machine.Pin.IN)
MINI_FAN = machine.Pin(18, machine.Pin.OUT)
#RELAY = machine.Pin(20, machine.Pin.OUT)

#     [ ] [ ] [ ] [ ] [ ]
# USB
#     [ ] [ ] [1] [2] [(3)]
#
# 1 BUTTON
# 2 MINI_FAN
# (3 RELAY)

Prev = 0
while True:    
    Btn = BUTTON.value()
    if Prev != Btn and Btn == 1:
        MINI_FAN.toggle()
    Prev = Btn