# p.188
# 関数の呼び出しの階層

def function_a():
    print('function_aの処理です')

def function_b():
    print('function_bの処理開始')
    function_a()
    print('function_bの処理終了')

print('function_bを呼び出します')
function_b()

