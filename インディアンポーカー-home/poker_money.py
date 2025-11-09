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
            return random.choice([8000, 8500, 9000, 9500, 10000])
        return 0
    elif 8 <= user_val <= 11:
        if is_fake:
            return random.choice([8000, 8500, 9000, 9500, 10000])
        return random.choice([4000, 5000, 6000])
    elif 2 <= user_val <= 7:
        if is_fake:
            return random.choice([3000, 4000, 5000])
        return random.choice([8000, 8500, 9000, 9500, 10000])

def judge(user, com, user_bet, com_bet):
    rewards = CHIP*2 + user_bet + com_bet
    global user_money
    global com_money
    com_val = 14 if com == 1 else com
    user_val = 14 if user == 1 else user
    if user_val > com_val:
        print('あなたの勝ちです。')
        print(f'あなたは{rewards}円を獲得しました。')
        user_money += rewards
        com_money -= rewards
    elif user_val < com_val:
        print('あなたの負けです。')
        print(f'あなたは{rewards}円を失いました。')
        user_money -= rewards
        com_money += rewards
    else:
        print('引き分けです。')
    

while True:
    print('--- プレイ ---')
    print('チップが2,000円支払われました。')
    com = random.randint(1, 13)
    user = random.randint(1, 13)
    com_bet = get_com_bet(user)
    com_money -= (CHIP + com_bet)
    print('相手の数字:', com)
    print(f'相手は{com_bet}円賭けました。')
    print(f'あなたの所持金: {user_money}')
    user_bet = int(input('何円賭けますか? (降りる 0) > '))
    user_money -= (CHIP + user_bet)
    print(f'あなた:{user} わたし:{com}')
    if user_bet > 0:
        judge(user, com, user_bet, com_bet)
    else:
        print('あなたは降りました。')
        print(f'あなたは{CHIP}円失いました。')
        user_money -= CHIP
        
    is_end = input('終わりたければ q :')
    if is_end.lower() == 'q':
        break
    
