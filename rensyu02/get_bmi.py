# 2.1.9 プログラムの記述

height = float(input('身長(cm)>'))
weight = float(input('体重(kg)>'))
height = height / 100.0
bmi = weight / (height * height)
print(bmi)
