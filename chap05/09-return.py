import random

def get_two_numbers():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    return (x, y)

a, b = get_two_numbers()
print(a, b)
