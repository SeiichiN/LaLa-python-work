# p271

f = open('visitor_record.txt', 'r', encoding='UTF-8')
lines = f.readlines()

for l in lines:
    print(l.rstrip('\n'))

f.close()
