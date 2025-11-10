# 数当てゲーム

import random

com = random.randint(1, 99)
print('わたしの考えた数字を当ててください')
print('1～99のどれかです')

while True:
    user = int(input('数字(1～99) > '))
    if user == com:
        print('あたりです')
        break
    elif user > com:
        print('大きすぎます')
    else:
        print('小さすぎます')

