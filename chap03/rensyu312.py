# 練習 3.1.2
# bodytype.py

height = float(input('身長(cm) > '))
weight = float(input('体重(kg) > '))
height = height / 100.0
bmi = weight / (height ** 2)

if bmi < 18.5:
    bodytype = 'やせ型'
elif bmi < 25.0:
    bodytype = '普通体重'
else:
    bodytype = '肥満'

print(f'BMI指数: {bmi:.2f}')
print(f'体型: {bodytype}')
