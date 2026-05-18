height = input('身長を入力してください(cm): ')
weight = input('体重を入力してください(kg): ')

height = float(height) / 100  # cmをmに変換
weight = float(weight)

bmi = weight / (height ** 2)
print('あなたのBMIは: {:.2f}'.format(bmi))
if bmi < 18.5:
    print('あなたは痩せ型です。')
elif 18.5 <= bmi < 25:
    print('あなたは普通体型です。')
else:  
    print('あなたは肥満体型です。')
print('身長: {:.2f} m'.format(height))
print('体重: {:.2f} kg'.format(weight))
print('BMI: {:.2f}'.format(bmi))
