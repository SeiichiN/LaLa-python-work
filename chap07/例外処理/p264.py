# 例外処理

try:
    print('a÷bの計算をします')
    a = input('aの値を入力してください: ')
    b = input('bの値を入力してください: ')
    # a, b は文字列
    c = float(a) / float(b)
    # float型に変換
    print('答えは', c)
except ValueError:
    print('入力が数字ではありません')
except ZeroDivisionError:
    print('ゼロで割ることはできません')
print('処理をおわります')
