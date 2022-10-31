name="aaa"
waist=84
age=44


print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

if age>=20 and waist>=58:
     print(name,"さん、モデル体型です")
else:
    print(name,"さんモデル体型ではありません" )

name=input("名前を教えて下さい")
