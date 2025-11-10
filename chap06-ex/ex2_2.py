# 問題2-2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 関数定義
def age_check(p, i):
    return p.age > i
    

a = Person('高橋太郎', 19)
b = Person('小林花子', 18)

# 関数呼び出し
if age_check(a, 18):
    print('18を超えている')
else:
    print('18以下である')
    
