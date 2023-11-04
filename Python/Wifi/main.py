import machine
import utime

import network
import socket

# ここに自分の Wifi 設定を書く
SSID = ''
PASSWORD = ''

# -3 network.STAT_WRONG_PASSWORD
# -2 network.STAT_NO_AP_FOUND
# -1 network.STAT_CONNECT_FAIL
#  0 network.STAT_IDLE
#  1 network.STAT_CONNECTING
#  3 network.STAT_GOT_IP
StatStr = {
    network.STAT_WRONG_PASSWORD:"WRONG_PASSWORD",
    network.STAT_NO_AP_FOUND:"NO_AP_FOUND",
    network.STAT_CONNECT_FAIL:"CONNECT_FAIL",
    network.STAT_IDLE:"IDLE",
    network.STAT_CONNECTING:"CONNECTING",
    network.STAT_GOT_IP:"GOT_IP"
}
def WaitForConnect():
    while True:#Limit > 0:
        print("Status =", StatStr[WLAN.status()])
        if WLAN.status() <= network.STAT_CONNECT_FAIL or WLAN.status() >= network.STAT_GOT_IP:
            print("Network connection failed")
            return
        utime.sleep(1)
    
WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(SSID, PASSWORD)

WaitForConnect()

if WLAN.status() != network.STAT_GOT_IP:
    raise RuntimeError('Network connection failed')
else:
    print('Connected')
    Status = WLAN.ifconfig()
    print( 'ip = ' + Status[0] )


