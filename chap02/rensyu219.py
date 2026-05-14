# 練習2.1.9
# get_bmi.py

# 身長を入力して、floatに変換
height = input('身長を入力(cm)')
height = float(height)

# 体重を入力して、floatに変換
weight = input('体重を入力(kg)')
weight = float(weight)

# mに換算
height = height / 100.0

bmi = weight / (height ** 2)
bmi = round(bmi, 1)
print(bmi)
