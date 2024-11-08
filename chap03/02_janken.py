import random
hand = ['グー', 'チョキ', 'パー']

while True:
    user = int(input('0:グー 1:チョキ 2:パー 9:終了 > '))
    if user == 9:
        break
    com = random.randint(0, 2)
    if user == com:
        result = 'あいこ'
    elif (user+1) % 3 == com:
        result = 'ユーザーの勝ち'
    else:
        result = 'わたしの勝ち'

    print(f'ユーザー：{hand[user]} わたし：{hand[com]}')
    print(result)
print('おつかれ～')
