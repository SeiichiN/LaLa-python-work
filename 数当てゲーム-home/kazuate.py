# 数当てゲーム

import random

com = random.randint(1, 99)

while True:
    user = int(input('1〜99 > '))
    if user == com:
        print('当たりです')
        break
    elif user > com:
        print('大きすぎます')
    else:
        print('小さすぎます')
    
