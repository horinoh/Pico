import machine
import utime

# RP2040 には温度センサーが内蔵されている
SENSOR = machine.ADC(4)

# u16 [0, 65535] を 電圧 [0, 3.3] へ変換する
def ToVoltage(u16Val):
    return u16Val * 3.3 / (65535)

# 電圧を摂氏へ変換する
def ToCelsius(Voltage):
   # Pico RP2040 データシートより、電圧値を摂氏へ変換するのは以下の式となる
   return 27 - (Voltage - 0.706) / 0.001721

while True:    
    Celsius = round(ToCelsius(ToVoltage(SENSOR.read_u16())), 1)
    print(Celsius)
    utime.sleep(1)