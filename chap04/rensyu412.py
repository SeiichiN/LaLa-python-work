# 練習 4.1.2
# get_temp.py

#temp = []
#for n in range(8, 18):
#    kion = float(input(f'{n}時の気温を入力してください > '))    
#    temp.append(kion)

temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]

for n in range(8, 18):
    print(f'{n}時の気温:{temp[n-8]}度')
    
sum = 0
for t in temp:
    sum += t
avg = sum / len(temp)
avg = round(avg, 1)
print(f'平均気温: {avg}度')
