# インディアンポーカー
#
# 所持金: 100,000
# 参加費:   2,000

import random

com_money = 100000
user_money = 100000
CHIP = 2000

def get_com_bet(user):
    val = random.randint(1, 5)
    if val == 1 or val == 5:
        is_fake = True
    else:
        is_fake = False
    user_val = 14 if user == 1 else user
    if user_val >= 12:
        if is_fake:
            return 10000
        return 0
    elif 8 <= user_val <= 11:
        if is_fake:
            return 10000
        return 5000
    elif 2 <= user_val <= 7:
        if is_fake:
            return 3000
        return 10000

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
    print('チップが2,000円支払われました。')
    com = random.randint(1, 13)
    user = random.randint(1, 13)
    com_bet = get_com_bet(user)
    print('相手の数字:', com)
    user_bet = int(input('何円賭けますか? (降りる 0)'))
    print(f'あなた:{user} わたし:{com}')
    if user_monay > 0:
        judge(user, com)
    else:
        print('あなたは降りました。')
        
    is_end = input('終わりたければ q :')
    if is_end.lower() == 'q':
        break
    
