# p.157
# 辞書

info = {
    'firstname' : '太郎',
    'lastname'  : '山田',
    'address'   : '茨城県つくば市 99-99',
    'age'       : 29,
    3           : '牛',
    }

# キーを一覧する
for k in info.keys():
    print(k)

# 値を一覧する
for v in info.values():
    print(v)

    
# キーと値のペアで一覧する
for i in info.items():
    print(i)

# アンパック代入して一覧する
for k, v in info.items():
    print(k, ':', v)
    
