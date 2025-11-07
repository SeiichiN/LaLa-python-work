# p194
# 引数が２つある関数

def countdown(start, end=0):
    print('１つめの引数:', start)
    print('２つめの引数:', end)
    print('カウントダウン')
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1
    print(counter)

countdown(7, 3)


            
    
    
