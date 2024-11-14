import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def toString(self):
        return self.suit + ':' + str(self.number)

card_list = []

for n in range(1, 14):
    card = Card("heart", n)
    card_list.append(card)
for n in range(1, 14):
    card = Card("spade", n)
    card_list.append(card)
for n in range(1, 14):
    card = Card("club", n)
    card_list.append(card)
for n in range(1, 14):
    card = Card("diamond", n)
    card_list.append(card)

card1 = random.choice(card_list)
print(card1.toString())
card_list.remove(card1)
print(len(card_list))

