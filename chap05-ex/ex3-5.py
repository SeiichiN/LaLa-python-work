#221
#問題3-5

def get_tail(*args):
    return args[-1]

print(get_tail(3,5,9,2))


def get_tail2(*args):
    n = len(args)
    return args[n-1]
    
print(get_tail2(3,5,9,2))
