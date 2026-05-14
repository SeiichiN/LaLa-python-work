# 練習2.1.6
import math

# 30度をラジアンに変える
sita = math.radians(30)

# 1 : tan(sita) = 20 : x
# 1 * x == 20 * tan(sita)
# x = 20 * tan(sita)
height = 20 * math.tan(sita)
print(height)
