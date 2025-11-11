import requests

html = requests.get('https://www.shoeisha.co.jp/book/ranking')
print(html.text)


# テキストを保存する
with open('sample.html', 'w', encoding='UTF-8') as f:
    for line in html.text:
        f.write(line)
        
    
