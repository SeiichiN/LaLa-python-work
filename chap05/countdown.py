# p193
# 引数のある関数

def countdown(start):
    print('関数が受け取った値:', start)
    print('カウントダウン')
    counter = start
    while counter >= 0:
        print(counter)
        counter -= 1
    print(counter)

countdown(3)
countdown(10)

            
    
    
