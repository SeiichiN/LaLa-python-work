def function_a():
    print('aの処理です')

def function_b():
    print('bの処理開始')
    function_a()
    print('bの処理終了')

print('bを呼び出します')
function_b()
