import calendar
day = int(input())
month = int(input())
year = int(input())

month_31_days = [1, 3, 5, 7, 8, 10, 12]
month_30_days = [4, 6, 9, 11]

if month in month_31_days:
    month_days = 31
elif month in month_30_days:
    month_days = 30
elif month == 2:
    if calendar.isleap(year) == True:
        month_days = 29
    else:
        month_days = 28

if day < month_days:
    day += 1
elif month < 12:
    day = 1
    month += 1  
else:
    day = 1
    month = 1
    year += 1

print(day, month, year, sep='.')
