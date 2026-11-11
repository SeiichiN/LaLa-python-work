# 4.1.5 トランプ

import random

cards = []
suits = ['heart', 'diamond', 'club', 'spade']

##for n in range(1, 14):
##    cards.append(('heart', n))
##    cards.append(('diamond', n))
##    cards.append(('club', n))
##    cards.append(('spade', n))

for s in suits:
    for n in range(1, 14):
        cards.append((s, n))
        
random.shuffle(cards)
card = random.choice(cards)
# card = cards.pop()
print(f'{card[0]}: {card[1]}')
cards.remove(card)
print(f'残ったカード: {len(cards)}枚')
