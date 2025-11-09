# インディアンポーカー

import random

def judge(user, com):
    com_val = 14 if com == 1 else com
    user_val = 14 if user == 1 else user
    if user_val > com_val:
        print('あなたの勝ちです。')
    elif user_val < com_val:
        print('あなたの負けです。')
    else:
        print('引き分けです。')
    

while True:
    com = random.randint(1, 13)
    user = random.randint(1, 13)

    print('相手の数字:', com)
    select = input('勝負しますか？ (y/n)')
    print(f'あなた:{user} わたし:{com}')
    if select.lower() == 'y':
        judge(user, com)
    else:
        print('あなたは降りました。')
    is_end = input('終わりたければ q :')
    if is_end.lower() == 'q':
        break
    
