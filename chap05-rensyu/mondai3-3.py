# 第5章練習問題
# 問題3-3

def get_message(name = '名無し'):
    return f'こんにちは{name}さん'

name = '浦島太郎'
msg = get_message(name);
print(msg)

msg = get_message();
print(msg)
