# p162
# セット集合

data = [1,2,3]  # リスト
a = set(data)   # セットに変換

data2 = [('a',1),('b',2),('c',3)]
b = set(data2)

data3 = {'b':'banana', 'a':'apple'}
c = set(data3)
# cはキーの集合

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C'}
set3 = {'A', 'D'}
result = set1.issubset(set2)
# set1 は set2 の中に含まれるか？
print(result)

result = set2.issubset(set1)
# set2 は set1 の中に含まれるか？
print(result)

result = set3.issubset(set1)
print(result)

