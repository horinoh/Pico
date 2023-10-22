# Pico

## Python
### 環境
- [Thonny](https://thonny.org/) をインストール
    - 起動して一番下の Configure interpreter ... から MicroPython (Raspberry Pi Pico) を選択
- ファームウェア
    - BOOTSEL ボタンを押しながら Windows と USB 接続する
    - RPI-RP2 フォルダがリムーバブルディスクとして現れるので、[INDEX.HTM を開く - MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)  からファームウェアをダウンロード
    - ダウンロードしたファームウェアを RPI-RP2 フォルダへドラッグ & ドロップ
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

### Grove
- [Grove](https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner%27s-Guide-for-Raspberry-Pi-Pico.pdf
)

## C++
### 環境
- [ドキュメント](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
- [pico-setup-windows](https://github.com/raspberrypi/pico-setup-windows) から pico-setup-windows-x64-standalone.exe をダウンロードして実行
    - サンプル (pico-examples) も取得しておく
- 環境変数 PICO_SDK_PATH をセットする、通常インストールなら以下のような場所になるはず
    ~~~
    C:\Program Files\Raspberry Pi\Pico SDK v1.5.1\pico-sdk
    ~~~

#### サンプルのビルド
- スタートメニューに Pico Developer Power Shell ができているので起動、以下のコマンドで VSCode を起動する
    ~~~
    $code
    ~~~
- VSCode で pico-examples フォルダを開く
- 一番下の青いツールバー
    - Kit の選択で "PICO ARM GCC Pico SDK Toolchain with GCC arm-none-eabi entry" を選択
- 左のサイドバーから CMake (三角アイコン)をクリック - ツリーからビルドしたい elf を選択 - 選択した右側にビルドのアイコンが出るのでクリックしてビルド
    - ツリーの一番上にある "Build All Projects" ボタンを押すと全ビルドになる

##### Pico W のサンプルをビルドするには
- 環境変数 PICO_BOARD をセットする (pico-examples 以下のファイルを書き換えたくないので、こちらを採用した)
    ~~~
    pico_w
    ~~~
- もしくは CMakeLists.txt に以下のように追記してもよい
    ~~~
    set(PICO_BOARD "pico_w")
    ~~~

#### 実行
- ビルド結果(.uf2, .elf)は pico-examples/build 以下に出力される
##### Debug (.elf)
- Debug Probe を接続
    - Pico wh の場合は SWD (Serial Wire Debug) があるので、Pico wh と Debug Probe を SWD で接続する
    - Debug Probe を PC と USB 接続する
    - Pico への USB 接続は単に電源供給目的
        - 間に Debug Probe を介して、PC と Pico が繋がる形となる
        - PC -(USB)- Debug Probe -(SWD)- Pico
- 左のサイドバーから Run and Debug (▶と虫)をクリック - 左側の上部に緑の▶があるので押す、もしくは F5
    - 初回は実行するターゲットの選択を促されるので選択して実行
    - 2回目以降、ターゲットを変更したい場合は、一番下の青いツールバー中央あたりにターゲット選択のボタンがあるのでそこで選択する
- 実行すると画面上部中央に操作パネルが出る (ほぼ Visual Studio と同じキーバインド)
    - Contine(F5), Step Over(F10), Steo Into(F11), Step Out(Shift + F11), 等...
- 出力 (printf)
    - 下半分のウインドウの上部にあるツールバー - "SERIAL MONITOR" を選択
    - シリアルデバイスで適切な COM を選択して - "Start Monitoring" を押すと出力される
        ~~~
        ---- Opened the serial port COM5 ----
        Hello, world!
        Hello, world!
        Hello, world!
        ...
        ~~~
##### Release (.uf2)
- BOOTSEL ボタンを押しながら Windows と USB 接続する
- .uf2 ファイルを RPI-RP2 フォルダへドラッグ & ドロップ

#### 自前環境のビルド 
- ここでは親フォルダを C とした
    - C 以下に pico-sdk/external/pico_sdk_import.cmake をコピーする
    - C 以下に pico-examples/.vscode をフォルダごとコピーする
    - C 以下に CMakeLists.txt を作る
- スタートメニューに Pico Developer Power Shell ができているので起動、以下のコマンドで VSCode を起動し、C フォルダを開く
    ~~~
    $code
    ~~~
    - 一番下の青いツールバー
        - Kit の選択で "GCC XXX arm-none-eabi" を選択
    - C 以下にサブフォルダ作成、ここでは Hello を例とする
        - Hello 直下に以下のファイルを作成する
            ~~~
            CMakeLists.txt
            main.c
            ~~~
#### 自前環境の実行
- 上記サンプルの実行と手順は同じ

