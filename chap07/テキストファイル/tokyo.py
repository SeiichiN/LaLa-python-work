# p.275

with open('tokyo.txt', 'w', encoding='UTF-8') as out_f:
    with open('visitor_record.txt', 'r', encoding='UTF-8') as in_f:
        for line in in_f:
            if '東京都' in line:
                out_f.write(line)
                