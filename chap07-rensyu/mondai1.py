# 練習問題
# 問題1

l = ['リンゴ', 'バナナ', 'オレンジ']
try:
    a = input('好きな整数(0～2)を入力してください:')
    print(l[int(a)])
except ValueError:
    print('数字ではありません')
except IndexError:
    print('範囲外の数字です')

