# p.194
# 引数が２つある関数

def countdown(start, end=3):
    print('1つめの引数:', start)
    print('2つめの引数:', end)
    print('カウントダウンをします')
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1

countdown(7)

    
