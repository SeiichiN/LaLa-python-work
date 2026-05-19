# temp_read_01.py

with open('temp.csv', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.rstrip('\n'))

print('終了します')
