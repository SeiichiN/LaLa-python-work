# 問題3-3

def get_message(name='名無し'):
    if name == '':
        name = '名無し'
    return f'こんにちは{name}さん'
    # return 'こんにちは' + name + 'さん'

name = input('名前 > ')
name = name.strip()
print(get_message(name))

