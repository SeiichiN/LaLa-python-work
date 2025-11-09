# じゃんけんゲーム

import random

def judge(user, com):
    if user == com:
        return 'あいこです'
    elif (user+1) % 3 == com:
        return 'あなたの勝ちです'
    else:
        return 'わたしの勝ちです'
    

msg = '0:グー 1:チョキ 2:パー >'
user = int(input(msg))
com = random.randrange(3)
result = judge(user, com)
hands = ('グー', 'チョキ', 'パー')
print(f'あなた:{hands[user]} わたし:{hands[com]}')
print(result)

