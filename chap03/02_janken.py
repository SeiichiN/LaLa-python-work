import random
user = int(input('0:グー 1:チョキ 2:パー > '))
com = random.randint(0, 2)
hand = ['グー', 'チョキ', 'パー']

if user == com:
    result = 'あいこ'
elif (user+1) % 3 == com:
    result = 'ユーザーの勝ち'
else:
    result = 'わたしの勝ち'

print(f'ユーザー：{hand[user]} わたし：{hand[com]}')
print(result)
