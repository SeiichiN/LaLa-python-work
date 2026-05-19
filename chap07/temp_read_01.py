# temp_read_01.py

f = open('temp.csv', 'r', encoding='UTF-8')
for line in f:
    print(line.rstrip('\n'))
f.close()

print('終了します')
