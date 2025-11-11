# じゃんけんゲーム

import random

def judge(user, com):
    if user == com:
        return 'あいこです'
    elif (user+1) % 3 == com:
        return 'あなたの勝ちです'
    else:
        return 'わたしの勝ちです'


def input_hand():
    while True:
        try:
            num =int(input('0:グー 1:チョキ 2:パー 9:終了 > '))
            if num in [0, 1, 2, 9]:
                return num
            else:
                print('数字が範囲外です')
        except:
            print('数字ではありません')
        

hands = ('グー', 'チョキ', 'パー')

while True:
    user = input_hand()
    if user == 9:
        break
    com = random.randrange(3)
    print(f'あなた:{hands[user]} わたし:{hands[com]}')
    print(judge(user, com))
    
print("終わります")
