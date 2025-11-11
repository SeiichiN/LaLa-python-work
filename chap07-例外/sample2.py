# 例外

print('a ÷ b の計算をします')

try:
    a = input('aの値を入力してください')
    b = input('bの値を入力してください')
    c = float(a) / float(b)
    print('答えは', c)
except ValueError:
    print('入力が文字です')
except ZeroDivisionError:
    print('0では割れません')
print('処理を終わります')



# ValueError: could not convert string to float: 'a'

# ZeroDivisionError: division by zero
