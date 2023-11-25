import machine
import utime

DOT_PERIOD_MS = 100
# モールスのパターン
MorseLetters = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
}

# モールスのパターンを LED 出力
def PutMorse(Pattern):
    for i in Pattern:
        LED.high()
        utime.sleep_ms(DOT_PERIOD_MS * (1 if i == "." else 3))
        LED.low()
        utime.sleep_ms(DOT_PERIOD_MS * 1);
    utime.sleep_ms(DOT_PERIOD_MS * 2);
        
# 文字列をモールスとして LED 出力
def ToMorse(Str):
    for i in Str.lower():
        if i.isalpha():
            Pattern = MorseLetters[i]
            PutMorse(Pattern)
            print(i, "==", Pattern)
        elif i.isspace():
            utime.sleep_ms(DOT_PERIOD_MS * 4);
            print(" ")

LED = machine.Pin("LED", machine.Pin.OUT)
Timer = machine.Timer()

def OnTimer(t) :
    global LED
    LED.toggle()
    print(LED.value())

ToMorse("Hello World")
Timer.init(freq = 2.5, mode = machine.Timer.PERIODIC, callback = OnTimer)
