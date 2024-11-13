# テキストファイルの読み書き

f = open('visitor_record.txt', 'r', encoding='UTF-8')
lines = f.readlines()

for l in lines:  # l = '2021-07-01,東京都,1,0\n'
    print(l.strip())

f.close()
