import machine

LED = machine.Pin("LED", machine.Pin.OUT)
Timer = machine.Timer()

def OnTimer(t) :
    global LED
    LED.toggle()
    print(LED.value())
    
Timer.init(freq = 2.5, mode = machine.Timer.PERIODIC, callback = OnTimer)
