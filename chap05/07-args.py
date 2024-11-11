def func_a(*args):  # タプル
    for a in args:
        print(a)

#func_a(1, 2)
#func_a(1, 2, 3, 4)

def func_b(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

func_b(a=1, b=2)
func_b(c=3, d=4, e=5, f=6)
#a = {'a': 1, 'b': 2}
#func_b(a)
