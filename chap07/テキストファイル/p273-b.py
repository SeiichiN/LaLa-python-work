# p.273
# with文

with open('data-b.txt', 'w', encoding='UTF-8') as f:
    for i in range(0,100):
        f.write(str(i) + '\n')
        