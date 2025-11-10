# 問題2-4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 関数定義
def get_total_age(p1, p2):
    return p1.age + p2.age
    

a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

# 関数呼び出し
total = get_total_age(a, b)
print(f'年齢の合計は{total}である')
