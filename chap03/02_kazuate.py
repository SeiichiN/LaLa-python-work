import random

com = random.randint(1, 99)
num = 0
while num != com: 
    num = int(input('1～99 > '))
    if num == com:
        msg = 'あたり'
    elif num > com:
        msg = '大きすぎます'
    else:
        msg = '小さすぎます'
    print(msg)

