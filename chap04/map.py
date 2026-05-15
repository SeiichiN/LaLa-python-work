# 4.3.7 2次元リスト

map = [
    ['.', 's', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'g', '.', '.'],
    ['#', '#', '.', 'p', '.'],
    ['e', '.', '.', '.', '.'],
    ]

map[2][1] = '@'

# print map
for row in range(5):
    print('|', end='')
    for col in range(5):
        print(map[row][col], end='|')
    print()
        
y = int(input('Y > '))
x = int(input('X > '))
print(f'{y}:{x}にあるのは{map[y][x]}です')

