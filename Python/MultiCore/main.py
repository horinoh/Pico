import machine
import _thread

def OnCore1():
    LED = machine.Pin("LED", machine.Pin.OUT)
    LED.high()
    
    print('OnCore1')

_thread.start_new_thread(OnCore1, ())