# マップを使ったゲーム

import random

map = [['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.']]

def look():
    print(f'[{py}:{px}]')
    print(map[py][px])
    

# プレーヤーの位置
py = random.randrange(5)
px = random.randrange(5)

# プレーヤーの場所の位置情報
look()

while True:
    # wsadのどれかを入力
    cmd = input('w↑s↓a←d→ q:end > ')
    if cmd == 'w':
        py = max(py-1, 0)
    elif cmd == 's':
        py = min(py+1, 4)
    elif cmd == 'a':
        px = max(px-1, 0)
    elif cmd == 'd':
        px = min(px+1, 4)
    elif cmd == 'q':
        break
    # 現在位置表示
    look()

print('Game End')    
