# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime
from datetime import date, timedelta
from datetime import time 


def month_days(year, month):
    m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_index = month - 1
    result = m_days[month_index]
    if 1 == month_index:
        if not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            result += 1
    return result;
 
now = datetime.now()
# this_month_days =  number of days in current month 
this_month_days = month_days(now.year, now.month)
 
print('This month has {0} days'.format(this_month_days))
d = timedelta(days = this_month_days)
date_n_days_ago = now - d
print('Today is {0}  month ago it was: {1}'.format(now, date_n_days_ago))

date_string = '01/01/17 12:10:03.234567'
date_dt = (datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')).strftime('%d/%m/%y %H:%M:%S.%f')
print ('this date is {0}'.format(date_dt))

i = timedelta(days = 1)
today = date.today()
yesterday = (today - i)
day_ago = str(yesterday)
print('Today is {0}'.format(today))
day_ago = datetime.strptime(day_ago, '%Y-%m-%d')
print('yesterday was: {0}'.format(day_ago))

