import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019,3,3))

print(calendar.monthcalendar(2019,3))

print(calendar.calendar(2019))

day_of_the_week = calendar.weekday(2020,3,8)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000,2004)
print(how_many_leap_days)