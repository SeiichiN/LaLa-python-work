# 練習 5.1.4

def is_leapyear(year):
    if year % 400 == 0:
        result = True
    else:
        if year % 4 == 0:
            if year % 100 == 0:
                result = False
            else:
                result = True
        else:
            result = False
    return result
                

def is_leapyear2(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    return False

def is_leapyear3(year):
    return year%400==0 or (year%4==0 and year%100!=0)
