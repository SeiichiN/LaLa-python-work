# 高階関数の例

def list_walk(lst, func):
    lst2 = []
    for n in lst:
        lst2.append(func(n))
    return lst2

def plus_one(x):
    return x+1

def twice(x):
    return x*2

def square(x):
    return x * x

lst = [1,2,3,4,5]
lst2 = list_walk(lst, plus_one)
print(lst2)
lst3 = list_walk(lst, two_times)
print(lst3)
