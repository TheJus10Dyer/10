# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:28:58 2022

@author: Justin
"""

import time

starttime = [3,22,2022,9,41,'AM']
minutes = starttime[4]
hour = starttime[3]
year = starttime[2]
day = starttime[1]
month = starttime[0]
period = starttime[5]
boottime = time.monotonic()
January = 31
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31
while True:
    if year%400 == 0 or year%4 == 0 and year%100 !=0:
        February = 29
    else:
        February = 28
    timestamp = [month,day,year,hour,minutes,period]
    runtime = (time.monotonic() - boottime)
    if runtime > 60:
        minutes = minutes + 1
        boottime = time.monotonic()
    if hour < 12:
        x = 1
    if minutes > 59:
        minutes = 0
        hour = hour + 1
        if hour == 12 and x == 1:
            x = 0
            if period == 'AM':
                period = 'PM'
                continue
            if period == 'PM':
                period = 'AM'
            if hour == 12 and period == 'AM':
                day = day + 1
        if hour == 13:
            hour = 1
    if month == 1:
        length = January
    if month == 2:
        length = February
    if month == 3:
        length = March
    if month == 4:
        length = April
    if month == 5:
        length = May
    if month == 6:
        length = June
    if month == 7:
        length = July
    if month == 8:
        length = August
    if month == 9:
        length = September
    if month == 10:
        length = October
    if month == 11:
        length = November
    if month == 12:
        length = December
    if day > length:
        day = 1
        month = month + 1
    if month == 13:
        month = 1
        year = year + 1
    print('Time-stamp:', ' ', month,'/',day,'/',year,'     ',hour,':',minutes,period)
    time.sleep(0.1)