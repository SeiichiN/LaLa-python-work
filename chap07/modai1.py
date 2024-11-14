# 問題1

lst = ['りんご', 'ばなな', 'オレンジ']
a = input('好きな整数を入力してください')
try:
    print(lst[int(a)])
except ValueError:
    print('数字が入力されませんでした')
except IndexError:
    print('範囲外の値が入力されました')
