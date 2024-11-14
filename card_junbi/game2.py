import random



card_list = []

for n in range(1, 14):
    card = ("heart", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("spade", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("club", n)
    card_list.append(card)
for n in range(1, 14):
    card = ("diamond", n)
    card_list.append(card)

card1 = random.choice(card_list)
print(card1)
card_list.remove(card1)
print(len(card_list))

