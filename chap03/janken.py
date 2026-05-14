# じゃんけんゲーム

import random

hands = ['グー', 'チョキ', 'パー']

com = random.choice(hands)
num = input('0:グー 1:チョキ 2:パーを入力 > ')
num = int(num)
user = hands[num]

print(f'あなた:{user} わたし:{com}')

if user == com:
    print('あいこです')
elif user == 'グー' and com == 'チョキ':
    print('あなたの勝ちです')
elif user == 'チョキ' and com == 'パー':
    print('あなたの勝ちです')
elif user == 'パー' and com == 'グー':
    print('あなたの勝ちです')
else:
    print('わたしの勝ちです')
    
    
