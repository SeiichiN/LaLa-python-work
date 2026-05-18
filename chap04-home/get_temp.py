temp = {}
for h in range(8, 18):
    hour = str(h) + '時'
    t = float(input(f'{hour}の気温 > '))
    temp[hour] = t
    
