import requests #HTTP通信用のPythonライブラリ

def savefunc(link_str, file_str, num):
    # 1から100までの画像を取得する場合は1,101で指定（pythonの範囲指定は以上未満の為）
    for i in range(1,int(num)):
        print(i)
        url = link_str.format(str(i)) #取得する画像URL https://www.hoge.jp/fuga{}.jpg のように記述
        
        file_name = file_str.format(str(i).zfill(3)) #保存するディレクトリとファイル名の指定 hoge/fuga{}.jpg のように記述

        response = requests.get(url) #サーバからurl内に格納された情報を取得
        image = response.content #情報の中身を代入

        with open(file_name, "wb") as f: #file_nameでファイルに書き込み操作を行う
            f.write(image)

print("取得する画像URLをhttps://www.hoge.jp/fuga{}.jpgのように記述せよ")
link_str = input()

print("保存するディレクトリとファイル名の指定 hoge/fuga{}.jpg のように記述せよ")
file_str = input()

print("保存する画像の枚数を指定せよ")
num = input()


savefunc(link_str, file_str, num)
