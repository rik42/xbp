import dfLink

#端末設定---------------------
#端末keyを指定してください。
pkey=''
#-------------------------------------------

#シリアルポートを入力-------------------------
serial_port=''
#-------------------------------------------
#Arduinoとのシリアル通信設定-------------------
my_arduino = dfLink.set_serial(serial_port,9600)
#-------------------------------------------

#while Trueは無限ループ#----------------------
while True:
    # Arduinoからreadlineコマンドでデータを取得し、data_from_arduinoという変数に格納
    data_from_arduino=my_arduino.readline()
    #stripコマンドで、data_from_arduinoの中の余計な文字を削除
    #さらにintで文字で送られてきたデータをint型に変換
    data=int(data_from_arduino.strip())
    print(data)

    # データの設定--------------------------------
    int_data = data #Arduinoから受け取った値をここでint_dataにいれる
    float_data = ""
    txt_data = ""
    # -------------------------------------------

    # データの送信---------------------------------
    # 整数データ:int_data
    # 実数データ(小数を含むデータ):float_data
    # テキストデータ:txt_data
    ret = dfLink.sendData_To_dfLink(int_data=int_data,float_data=float_data,text_data=txt_data,pkey=pkey)
    print(ret)
    # -------------------------------------------
#-------------------------------------------