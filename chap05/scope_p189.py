# p.189
# 変数のスコープ

a = 10
def function_a():
    # global a
    a = 20
    print(a)  # 20

function_a()
print(a)  # 10
