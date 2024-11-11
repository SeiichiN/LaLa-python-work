def countdown(start, end=0):
    print('関数が受け取った値1:', start)
    print('関数が受け取った値2:', end)
    print('カウントダウンします')
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1
countdown(end=3, start=7)
countdown(10)

