# 問題2-2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 関数定義
def print_younger_person_name(p1, p2):
    if p1.age <= p2.age:
        return p1.name
    return p2.name
    

a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

# 関数呼び出し
name = print_younger_person_name(a, b)
print(f'年齢が若いのは{name}である')
