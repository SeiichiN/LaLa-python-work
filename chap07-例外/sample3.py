# 例外

print('a ÷ b の計算をします')

a = input('aの値を入力してください')
b = input('bの値を入力してください')
try:
    c = float(a) / float(b)
except ValueError:
    print('入力が文字です')
except ZeroDivisionError:
    print('0では割れません')
else:
    print('答えは', c)
    
print('処理を終わります')



