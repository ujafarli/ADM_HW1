import calendar

#using calendar library, find x which shows number from 0 to 6( 7 days of week)
user_input = input().split()

x = calendar.weekday(int(user_input[2]), int(user_input[0]), int(user_input[1]))

#then according to number print name of that day in a week
if x == 0:
    print("MONDAY")
elif x == 1:
    print("TUESDAY")
elif x == 2:
    print("WEDNESDAY")
elif x == 3:
    print("THURSDAY")
elif x == 4:
    print("FRIDAY")
elif x == 5:
    print("SATURDAY")
elif x == 6:
    print("SUNDAY")
