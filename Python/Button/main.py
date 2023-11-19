import machine

LED = machine.Pin("LED", machine.Pin.OUT)

Prev = LED.value()
while True:
    Btn = rp2.bootsel_button()
    if Prev != Btn:
        LED.value(Btn)
        print(LED.value())
    Prev = Btn



