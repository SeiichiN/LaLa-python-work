# 年号から西暦を求める

from nengos import nengos

nengo = input('年号 > ')
nen   = int(input('年 > '))
seireki = nengos[nengo] + nen - 1
print(f'{nengo} {nen}年は、西暦{seireki}年')
