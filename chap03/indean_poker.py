import random

user = random.randint(1, 13)
com = random.randint(1, 13)
usernum = 14 if user == 1 else user
comnum = 14 if com == 1 else com

print(f"comの数字:{com}")
if usernum < 5:
    print('(^_^)')
elif 7 < usernum < 10:
    print('(-_-)')
elif 9 < usernum < 14:
    print('(*o*)')
else:
    print('(X_X)')
print("勝負しますか？")
select = input('y/n > ')
if select == 'y':
    if usernum == comnum:
        msg = '引き分け'
    elif usernum > comnum:
        msg = 'あなたの勝ち'
    else:
        msg = 'わたしの勝ち'
else:
    msg = 'びびりですか？'
print(f'あなた：{user} わたし：{com}')
print(msg)
