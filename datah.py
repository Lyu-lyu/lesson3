# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime
from datetime import date, timedelta
from datetime import time 


def month_days_amount(year, month):
	# list of the days in months 
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # to get index in list we minus 1
    month_index = month - 1
    month_days_for_counting = month_days[month_index]
    # finding how many days february lasts
    if month_index == 1:
    	# checking if it is a leap-year
        if not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            month_days_for_counting += 1
    # returning 28 if it isn't a leap-year
    return month_days_for_counting
 

now = datetime.now()
# this_month_days =  number of days in current month 
this_month_days = month_days_amount(now.year, now.month)
 
print('This month has {0} days'.format(this_month_days))
amount_of_days_delta = timedelta(days = this_month_days)
date_n_days_ago = now - amount_of_days_delta 
print('Today is {0}  month ago it was: {1}'.format(now, date_n_days_ago))

date_string = '01/01/17 12:10:03.234567'
# the second strftime defines the format date output
date_dt = (datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f'))
print ('this date is {0}'.format(date_dt))

days_delta = timedelta(days = 1)
today = date.today()
yesterday = (today - days_delta)
day_ago = str(yesterday)
print('Today is {0}'.format(today))
day_ago = datetime.strptime(day_ago, '%Y-%m-%d')
print('yesterday was: {0}'.format(day_ago))


if  name ==  "__main__" :
    main()

