def is_leap(year):
    leap = False
    
# if year is divisible by 400 is leap year
    if (year % 400 == 0):
        leap = True
# not divisible by 400, but divisible by 100 then not leap year
    elif (year % 100 == 0) :
        leap = False
# Divisible by 4 is a leap year
    elif (year % 4 == 0) :
        leap = True
    return leap

year = int(input())
print(is_leap(year))
