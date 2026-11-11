# 3.1.2 if文

height = float(input('身長 > ')) / 100.0
weight = float(input('体重 > '))
bmi = weight / (height * height)
print(f'bmi: {bmi}')
if bmi < 18.5:
    bodytype = 'やせ型'
elif bmi < 25.0:
    bodytype = '普通体重'
else:
    bodytype = '肥満'
print('体型: ' + bodytype)



    
