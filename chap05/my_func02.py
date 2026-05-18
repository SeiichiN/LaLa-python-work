# my_func02.py

def plus_one(lst):
    for i in range(len(lst)):
        lst[i] += 1

a = [1,2,3]
plus_one(a)
print(a)   #[2, 3, 4]
