import random

com = random.randint(1, 9)

num = int(input('1～9 > '))

if num == com:
    msg = 'あたり'
elif num > com:
    msg = '大きすぎます'
else:
    msg = '小さすぎます'

print(msg)
