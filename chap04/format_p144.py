# p.144
# strクラスのformatメソッド

year = 2025
month = 5
day = 14
moji = '今日は{}年{}月{}日です'
message = moji.format(year, month, day)
print(message)

moji = '今日は{1}月{2}日です。西暦{0}年。'
message = moji.format(year, month, day)
print(message)
