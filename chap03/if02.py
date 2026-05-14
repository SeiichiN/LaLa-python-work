year = int(input('年号を入力>'))

if 1926 <= year < 1989:
    print('昭和')
elif 1989 <= year < 2019:
    print('平成')
elif 2019 <= year <= 2026:
    print('令和')
else:
    print('範囲外です')

    
