# じゃんけんゲーム

import random

def judge(user, com):
    if user == com:
        return 'あいこです'
    elif (user+1) % 3 == com:
        return 'あなたの勝ちです'
    else:
        return 'わたしの勝ちです'
        
def get_number():
    is_number = False
    while not is_number:
        try:
            num = int(input('0:グー 1:チョキ 2:パー 9:終了 > '))
            is_number = True
        except:
            print('数字を入力してください')
    return num    


hands = ('グー', 'チョキ', 'パー')

while True:
    user = get_number()
    if user == 9:
        break
    com = random.randrange(3)
    print(f'あなた:{hands[user]} わたし:{hands[com]}')
    print(judge(user, com))
    
print("終わります")
