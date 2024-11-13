# 例外処理

print('a÷bの計算をします')
try:
    a = input('aの値を入力してください: ')
    b = input('bの値を入力してください: ')
    c = float(a) / float(b)
except ValueError:
    print('入力が数字ではありません')
except ZeroDivisionError:
    print('ゼロで割ることはできません')
else:
    print('答えは', c)
finally:
    print('処理を終わります')

print('end')
