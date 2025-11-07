#p213
# 問題3-1

def print_hello(count):
    while (count > 0):
        print('Hello')
        count -= 1

print_hello(3)


def print_hello2(count):
    for n in range(count):
        print('Hello')

print_hello2(3)
