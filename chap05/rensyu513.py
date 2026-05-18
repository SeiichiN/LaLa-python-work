# 練習 5.1.3

def get_message(name='名無し'):
    # return f'こんにちは{name}さん'
    # return "こんにちは{}さん".format(name)
    return 'こんにちは' + name + 'さん'

print(get_message('次郎'))
print(get_message())
