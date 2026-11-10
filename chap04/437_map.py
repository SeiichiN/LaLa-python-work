# 4.3.7 2次元リスト

map = [
    ['.', '#', '.', '.', '.'],
    ['.', '.', 's', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', 'p', '.', '.', 'g'],
    ['.', '.', 'e', '#', '.'],
    ]

# print('mapの情報を調べる')
# y = int(input('Y > '))
# x = int(input('X > '))
# print(f'{y}:{x}にあるのは{map[y][x]}です')

# プレイヤーの位置
ypos = 3
xpos = 2

# mapの基本
for y in range(5):
    for x in range(5):
        print(map[y][x])

# print map
##for y in range(5):
##    print("|", end="")
##    for x in range(5):
##        if y == ypos and x == xpos:
##            print('@', end="|")
##        else:
##            print(map[y][x], end="|")
##    print()
    
        
