# 5.1.4 うるう年の判定

def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

while True:
    year = int(input('西暦 > '))
    if year == 9:
        break
    if (is_leapyear(year)):
        print('うるう年です')
    else:
        print('うるう年ではありません')

print('bye')
