# じゃんけんゲーム

import random

def judge(user, com):
    if user == com:
        return 'あいこです'
    elif (user+1) % 3 == com:
        return 'あなたの勝ちです'
    else:
        return 'わたしの勝ちです'
        

hands = ('グー', 'チョキ', 'パー')

while True:
    user = int(input('0:グー 1:チョキ 2:パー 9:終了 > '))
    if user == 9:
        break
    com = random.randrange(3)
    print(f'あなた:{hands[user]} わたし:{hands[com]}')
    print(judge(user, com))
    
print("終わります")
