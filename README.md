# Pico

## Grove
- [Grove](https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner%27s-Guide-for-Raspberry-Pi-Pico.pdf
)

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
- [ドキュメント](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
- [pico-setup-windows](https://github.com/raspberrypi/pico-setup-windows) から pico-setup-windows-x64-standalone.exe をダウンロードして実行
    - サンプル (pico-examples) も取得しておく
- 環境変数 PICO_SDK_PATH をセットする
    - 通常インストールなら以下のような場所になるはず
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
    - Kit の選択で PICO ARM GCC Pico SDK Toolchain with GCC arm-none-eabi entry を選択
- 左のサイドバーから CMake (三角アイコン)をクリック - ツリーからビルドしたい elf を選択 - 選択した右側にビルドのアイコンが出るのでクリックしてビルド
    - ツリーの一番上にある Build All Projects ボタンを押すと全ビルドになる

##### Pico W のビルド
- pico_w のビルドをするには 環境変数 PICO_BOARD  をセットする
    ~~~
    pico_w
    ~~~
- もしくは CMakeLists.txt に以下のように追記してもよい
    ~~~
    set(PICO_BOARD "pico_w")
    ~~~
    - pico-examples 以下のファイルを書き換えたくないので環境変数を採用した

#### サンプルの実行
- ビルド結果(.uf2, .elf)は pico-examples/build 以下に出力される

##### Debug (.elf)
- 左のサイドバーから Run and Debug (▶と虫)をクリック - 左側の上部に緑の▶があるので押す - 初回は実行するターゲットの選択を促されるので選択して実行
- ターゲットを変更したい場合(2回目以降)は、一番下の青いツールバー中央あたりにターゲット選択のボタンがあるのでそこで選択する

##### Release (.uf2)
- BOOTSEL ボタンを押しながら Windows と USB 接続する
- RPI-RP2 フォルダがリムーバブルディスクとして現れるので、.uf2 ファイルをコピーする

### 開発
- ここでは親フォルダを C とした
    - C 以下に pico-sdk/external/pico_sdk_import.cmake をコピーする
    - C 以下に pico-examples/.vscode をフォルダごとコピーする
    - C 以下に CMakeLists.txt を作る
- スタートメニューに Pico Developer Power Shell ができているので起動、以下のコマンドで VSCode を起動し、C フォルダを開く
    ~~~
    $code
    ~~~
    - 一番下の青いツールバー
        - Kit の選択で GCC XXX arm-none-eabi を選択
    - C 以下にサブフォルダ作成、ここでは Hello とする
        - Hello 直下に以下のファイルを作成する
            ~~~
            CMakeLists.txt
            main.c
            ~~~

### デバッグ
<!--
- 接続
    - Pico と [Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) を SWD(Serial Wire Debug) 接続する
    - Debug Probe の USB を PC と接続
    - Pico の USB は給電用
- 左のサイドバーから Run and Debug - 左上部の緑の▶でデバッグ開始
-->
