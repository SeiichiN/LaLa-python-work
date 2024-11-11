def function_a():
    global a
    a = 5
    print(a)   # 5

a=10
function_a()
print(a)       # 10
