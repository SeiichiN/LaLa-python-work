# 問題2-1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def age_check(p, age):
    return p.age >= age

a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

if age_check(a, 18):
    print(f"{a.name}は投票できます")
else:
    print(f"{a.name}は無理っす")
