# 問題2-1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_younger_person_name(p1, p2):
    if p1.age <= p2.age:
        print(p1.name)
    else:
        print(p2.name)
    

a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

print_younger_person_name(a, b)
