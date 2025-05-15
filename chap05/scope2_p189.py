# p.189
# 変数のスコープ

def function_a(b):
    b = 20
    print(b)  # 20

a = 10
function_a(a)
print(a)      # 10
