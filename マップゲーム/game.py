# マップを使ったゲーム

import random

map = [['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.']]

# プレーヤーの位置
py = random.randrange(5)
px = random.randrange(5)

# プレーヤーの場所の位置情報
print(f'[{py}:{px}]')
print(map[py][px])

while True:
    # wsadのどれかを入力
    cmd = input('w↑s↓a←d→ > ')
    # w -- ↑
    # s -- ↓
    # a -- ←
    # d -- →
    # 現在位置表示
    
