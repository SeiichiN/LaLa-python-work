# 3.1.3 if文とwhile文
# kazuate2

import random

com = random.randint(1, 99)
user = -1

while com != user:
    user = int(input('1～99の中から入力してください > '))
    if com < user:
        print('大きすぎます')
    elif com > user:
        print('小さすぎます')

print('正解です')
print('END')
