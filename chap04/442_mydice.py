# 4.4.2 タプルの利用
# 関数の戻り値としてタプルを使う

import random

def my_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    return a, b, c

x,y,z = my_dice()
print(x,y,z)

