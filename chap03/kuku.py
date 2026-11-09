# 3.6 二重ループ

for row in range(1, 10):
    for col in range(1, 10):
        print(f'{col}X{row}={col*row:2d}', end=' ')
    print()
    
