# 5.4.1 モジュール

from random import choice

menu = ["カレーライス", "お好み焼き", "天ぷらうどん", "寿司"]
places = ["McDonalds", "KFC", "Burger King", "Wendys", "Pizza Hut"]


def get_menu():
    """メニューを選ぶ"""
    return choice(menu)
                   
def get_shop():
    """ファストフードを選ぶ"""
    return choice(places)

print('__name__:', __name__)
# shop.pyを動作させた場合 -- '__main__'
# shop.pyが他から読み込まれた場合 -- モジュール名(shop)

# テスト目的
if __name__ == '__main__':
    print(f'ランチは{get_menu()}で決まり!')
    print(f'ファストフードは{get_shop()}がいいな!')
