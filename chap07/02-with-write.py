with open('number2.txt',
          'w',
          encoding='UTF-8') as f:
    for i in range(0, 100):
        f.write(str(i) + '\n')

# 自動でクローズ
