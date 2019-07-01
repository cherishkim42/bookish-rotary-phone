#leap year
#https://exercism.io/my/solutions/514424c1fbd542bc972f5a33c1ea2096

'''Given a year, report if it is a leap year.'''

def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(leap(1997))
    print(leap(1996))
    print(leap(1900))
    print(leap(2000))