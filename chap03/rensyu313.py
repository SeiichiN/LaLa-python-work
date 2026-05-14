# 練習 3.1.3
# kazuate.py

import random

com = random.randint(1, 99)

while True:
    user = input('1～99のどれかを入力 > ')
    user = int(user)

    if user == com:
        print('正解です')
        break
    elif user > com:
        print('大きすぎます')
    else:
        print('小さすぎます')
        
print('終了します')
    
