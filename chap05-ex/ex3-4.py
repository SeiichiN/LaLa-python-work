#219
#問題3-4

def get_absolute_value(value):
    return abs(value)

print(get_absolute_value(5.2))
print(get_absolute_value(-3.3))

def get_absolute_value2(value):
    if value < 0:
        value *= -1
    return value

print(get_absolute_value2(5.2))
print(get_absolute_value2(-3.3))
