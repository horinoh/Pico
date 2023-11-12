import machine
import utime

import network
import socket

# ここに自分の Wifi 設定を書く
# 5G の Wifi には対応していないので注意
SSID = ''
PASSWORD = ''

# 接続を待つ
def WaitForConnect():
    while True:
        # 成功 or 失敗が確定した
        if WLAN.status() <= network.STAT_CONNECT_FAIL or WLAN.status() >= network.STAT_GOT_IP:
            return
        
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
        print("Status =", StatStr[WLAN.status()])
        utime.sleep(1)

# ステーション用
WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(SSID, PASSWORD)

# アクセスポイント用
#WLAN = network.WLAN(network.AP_IF)

# 接続を待つ
WaitForConnect()

if WLAN.status() != network.STAT_GOT_IP:
    raise RuntimeError('Network connection failed')
else:
    print('ifconfig')
    Status = WLAN.ifconfig()
    IfConfigStr = { 0:"IP", 1:"SubNetMask", 2:"GateWay", 3:"DNSServer", }
    for i in range(len(Status)):
        print('	 ', IfConfigStr[i], '=', Status[i])

print('getaddrinfo')
AddrInfo = socket.getaddrinfo('0.0.0.0', 80)
AddrInfoStr = { 0:"Family", 1:"Type", 2:"Proto", 3:"Canonname", 4:"Sockaddr", }
for i in range(len(AddrInfo)):
    print('	 ', AddrInfoStr[i], '=', AddrInfo[i])

Addr = AddrInfo[0][-1]
print('Addr =', Addr)
Socket = socket.socket()
Socket.bind(Addr)
Socket.listen(1)

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>%s</p>
    </body>
</html>
"""

while True:
    try:
        # 接続を受け付ける (Conn, Address) のペアを返す
        # バインド、リッスン済みであること
        Conn, Address = Socket.accept()
        print('client connected from', Address)
        
        # ソケットからデータを受信、byte オブジェクトで返す
        Request = Conn.recv(1024)
        print(Request)

        Request = str(Request)
        LEDOn = Request.find('/light/on')
        LEDOff = Request.find('/light/off')
        print('led on = ' + str(LEDOn))
        print('led off = ' + str(LEDOff))

        if LEDOn == 6:
            print("led on")
            #led.value(1)
            #Stateis = "LED is ON"
        if LEDOff == 6:
            print("led off")
            #led.value(0)
            #Stateis = "LED is OFF"
            
        Response = html % Stateis
        # ソケットにデータを送信
        Conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        Conn.send(Response)
        Conn.close()

    except OSError as e:
        Conn.close()
        print('connection closed')


