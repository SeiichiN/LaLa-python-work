# 練習 4.1.5

import random

cards = []
suits = ['heart', 'diamond', 'club', 'spade']

for s in suits:
    for n in range(1, 14):
        cards.append((s, n))
        
random.shuffle(cards)
card = random.choice(cards)
print(card)
cards.remove(card)
print(f'残ったカード: {len(cards)}枚')
