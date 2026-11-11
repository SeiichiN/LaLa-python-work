# 西暦から年号へ

from nengos import nengos

sorted_nengos = sorted(nengos.items(),
                       key=lambda x: x[1])
# タプルのリスト

seireki = int(input('西暦 > '))

for k, v in sorted_nengos:
    if seireki > v:
        nengo = k
        nen = seireki - v + 1
        
print(f'西暦{seireki}年は、{nengo} {nen}年')
    
