# 問題3-5

def get_tail(*args):
    # args はタプル
    return args[-1]


last = get_tail(3,5,9,2,10, 5, 7)
print(last)
