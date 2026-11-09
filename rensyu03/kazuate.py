# 3.1.3 if文とwhile文

import random

com = random.randint(1, 99)

while True:
    user = int(input('1～99の中から入力してください > '))
    if com == user:
        print('正解です')
        break
    elif com < user:
        print('大きすぎます')
    elif com > user:
        print('小さすぎます')
print('END')
