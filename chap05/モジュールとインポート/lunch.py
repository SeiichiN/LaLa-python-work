# lunch.py

from shop import get_menu, get_shop

menu = get_menu()
fastfood = get_shop()

print(f'ファストフードなら{fastfood}がいいな')
print(f'本格的にランチなら{menu}がいいな')
