html = '''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>sample</title>
</head>
<body>
  <h1>sample</h1>
  <p>This is sample</p>
</body>
</html>
'''

print(html)

with open('html.txt', 'w', encoding='UTF-8') as f:
    for line in html:
        f.write(line)
        
    
