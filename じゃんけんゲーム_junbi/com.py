# comモジュール

import random

comHand = random.randint(0, 2)
userHand = 0
hand = ['グー', 'チョキ', 'パー']

def judge(userHand, comHand):
    if (userHand == comHand):
        msg = 'あいこです'
    elif (userHand+1) % 3 == comHand:
        msg = 'あなたの勝ちです'
    else:
        msg = 'わたしの勝ちです'
    message = f'あなた:{hand[userHand]} '
    message += f'わたし:{hand[comHand]} '
    message += msg
    return message

