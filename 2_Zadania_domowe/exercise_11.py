from datetime import date

t = date.today()

def format_date(day, month, year):
    if month == 1 and 0 < day < 32:
        return "%s %s %s" %(day, month, year)
    elif month == 2 and 0 < day < 29:
        return "%s %s %s" % (day, month, year)
    elif month == 3 and 0 < day < 32:
        return "%s %s %s" % (day, month, year)
    elif month == 4 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 5 and 0 < day < 32:
        return "%s %s %s" % (day, month, year)
    elif month == 6 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 7 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 8 and 0 < day < 32:
        return "%s %s %s" % (day, month, year)
    elif month == 9 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 10 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 11 and 0 < day < 31:
        return "%s %s %s" % (day, month, year)
    elif month == 12 and 0 < day < 32:
        return "%s %s %s" % (day, month, year)
    else:
        return None

day = 26
month = 3
year = 2000

data1 =format_date(day, month, year)

print(data1)

