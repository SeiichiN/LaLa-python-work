# p.160
# 並び替え

data = {
    'b' : 5,
    'c' : 2,
    'a' : 8,
    'd' : 7,
    }
newData = sorted(data.items())
# キーで並び替える
# 辞書ではなくなる。
# タプルのリストになる

newData2 = sorted(data.items(), key=lambda x:x[1])
