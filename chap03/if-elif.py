# p.102

age = int(input('年齢を入力\n'))
if age < 4:
    print('入場料は無料です')
elif age < 13:
    print('子ども料金で入場できます')
else:
    print('大人料金が必要です')