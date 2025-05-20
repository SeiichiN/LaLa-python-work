# 第6章練習問題
# 問題2-4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_total_age(p1, p2):
    return p1.age + p2.age


a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

total = get_total_age(a, b)
print(f'2人の年齢の合計は{total}です')

