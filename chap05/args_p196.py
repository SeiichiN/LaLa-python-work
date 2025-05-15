# p.196
# 可変長引数

def func_a(*args):
    for a in args:
        print(a, end=' ')

func_a(1, 2)
print()
func_a(1,2,3,4)
