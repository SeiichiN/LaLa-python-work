# 問題3-2

def get_rectangle_area(width, height):
    return width * height

width = float(input('幅 > '))
height = float(input('高さ > '))
area = get_rectangle_area(width, height)
print(f'幅{width} 高さ{height} の')
print(f'長方形の面積は{area}')
