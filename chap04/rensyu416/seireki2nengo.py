from nengos import nengos

nengos_sorted = sorted(nengos.items(),
                       key=lambda x:x[1],
                       reverse=False)
seireki = int(input('西暦を入力 > '))
for k, v in nengos_sorted:
    if v <= seireki:
        nengo = k
        nen = seireki - v + 1
print(f'{nengo} {nen}年')
