age = input('年齢を入力 > ')
age = int(age)

if age < 20:
    print('まだお酒は飲めません')
    print('お酒は20歳から飲めます')
elif age > 60:
    print('お酒の量は控えめにしましょう')
else:
    print('飲みすぎに注意しましょう')
    
print('終わります')
