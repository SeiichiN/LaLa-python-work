# 3.1.1 単純なif文

age = int(input('年齢を入力 > '))

if age < 20:
    print('まだお酒は飲めません')
    print('お酒は20歳から飲めます')
elif age > 50:
    print('お酒の量は控えめにしましょう')
else:
    print('飲みすぎに注意しましょう')
print('終わります')

