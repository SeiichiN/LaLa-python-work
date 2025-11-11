import requests
from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='UTF-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
print(soup.title)

for sec in soup.select('section'):
    if (sec.select_one('h2')):
        category = sec.select_one('h2').text
        title = sec.select_one('ul').select_one('li').text
        print('カテゴリ:', category)
        print('書籍名:', title[3:])
        
