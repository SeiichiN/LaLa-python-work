# 第5章練習問題
# 問題3-2

def get_rectangle_area(width,height):
    return width * height

width = 12.4
height = 23.5
area = get_rectangle_area(width,height)
message = '幅{}cm、高さ{}cmの三角形の面積は{}cm2'.format(width,height,area)
print(message)          
