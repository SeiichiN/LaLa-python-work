# 第6章練習問題
# 問題2-12

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def age_check(p, i):
    return p.age > i


a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

print(f'{a.name}さんの年齢は')
if age_check(a, 20):
    print('20歳を超えてます')
else:
    print('20歳以下です')

