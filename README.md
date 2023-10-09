# Pico

## Grove
- [Grove](https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner%27s-Guide-for-Raspberry-Pi-Pico.pdf
)

## デバッグ
- [Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html)

## Python
### 環境
- [Thonny](https://thonny.org/) をインストール
    - 起動して一番下の Configure interpreter ... から MicroPython (Raspberry Pi Pico) を選択
- ファームウェア
    - BOOTSEL ボタンを押しながら Windows と USB 接続する
    - RPI-RP2 フォルダがリムーバブルディスクとして現れるので、INDEX.HTM を開く - MicroPython からファームウェアをダウンロード
    - ダウンロードしたファームウェアを RPI-RP2 フォルダへドラッグ
<!--
- ライブラリ
    - [16x2 LCD Library](http://47.106.166.129/Embeded/pico-micropython-grove/blob/master/I2C/lcd1602.py)
        - Thonny から Save as で Pico へコピーしておく
    - [Temperature Humidity Sensor Library](http://47.106.166.129/Embeded/pico-micropython-grove/blob/master/I2C/dht20.py)
         - Thonny から Save as で Pico へコピーしておく
-->
<!--
    - [Temperature Humidity Sensor Library](http://47.106.166.129/Embeded/pico-micropython-grove/blob/master/Digital/dht11.py)
         - Thonny から Save as で Pico へコピーしておく
-->
### 開発
- Pico を PC と USB で接続 - Thonny を立ち上げる - ツールバーから Stop/Restart back-end process ボタンを押す - シェルエリアに出力が出れば成功

## C++
### 環境
### 開発
