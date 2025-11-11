# p273 書き出し

f = open('rensyu.csv', 'w', encoding='UTF-8')

for i in range(100):
    f.write(str(i) + '\n')

f.close()
