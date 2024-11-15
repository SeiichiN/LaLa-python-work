import random

def judge(oya, user):
    if oya[1] == 1 and user[1] == 1:
        return 'draw'
    elif oya[1] == 1 and user[1] != 1:
        return 'oya'
    elif oya[1] != 1 and user[1] == 1:
        return 'user'
    elif oya[1] > user[1]:
        return 'oya'
    elif oya[1] < user[1]:
        return 'user'
    else:
        return 'draw'

def print_card(oya, user):
    print(f'親 {oya}', end=' ')
    print(f'子 {user}')


card_list = []

for n in range(1, 14):
    card = ("heart", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("spade", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("club", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("diamond", n)
    card_list.append(card)


while True:
    oya = random.choice(card_list)
    card_list.remove(oya)

    user = random.choice(card_list)
    card_list.remove(user)

    print(oya)
    print('y:勝負する n:おりる q:やめる')
    select = input('> ').strip().lower()
    if select == 'y':
        winner = judge(oya, user)
        print_card(oya, user)
        print(winner)
    elif select == 'q':
        break
    else:
        print_card(oya,user)    
        print('チップ300円を支払った')

