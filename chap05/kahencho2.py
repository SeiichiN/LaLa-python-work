# p196
# 可変長引数
# 辞書

def func_b(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

#func_b(a=1, b=2)

def func_c(dic):
    for k,v in dic.items():
        print(k,v)

adic = {'a': 1, 'b': 2}
func_c(adic)
