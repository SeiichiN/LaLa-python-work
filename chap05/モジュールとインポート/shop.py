# shop.py

from random import choice 

menu = ['カレーライス', 'お好み焼き', '天ぷらうどん', '寿司']
places = ['McDonalds', 'KFC', 'Burger King', 'Wendys', 'Pizza Hut']

def get_menu():
    """メニューを選ぶ"""
    return choice(menu)

def get_shop():
    """ファストフードを選ぶ"""
    return choice(places)

if __name__ == '__main__':
    print(f'ランチは{get_menu()}で決まり！')
    print(f'ファストフードは{get_shop()}がいいな')

