# docstring.py
# (shop.py)

from random import choice

def get_menu():
    """メニューを選ぶ
       ４つの料理から選ぶ"""
    return choice(["カレーライス",
                   "お好み焼き",
                   "天ぷらうどん",
                   "寿司"])

menu = get_menu()
print(f'ランチは{menu}で決まり')
