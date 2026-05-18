# 練習 5.1.4

def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    return False
