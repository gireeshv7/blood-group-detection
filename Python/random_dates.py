import random
import time
from datetime import datetime

# def strTimeProp(start, end, format, prop):
#
#     stime = time.mktime(time.strptime(start, format))
#     etime = time.mktime(time.strptime(end, format))
#
#     ptime = stime + prop * (etime - stime)
#
#     return time.strftime(format, time.localtime(ptime))
#
#
# def randomDate(start, end, prop):
#     return strTimeProp(start, end, '%m/%d/%Y', prop)
#
# dates = randomDate("1/1/2008", "1/1/2009", 100)
# print(dates)


year = random.randint(1950, 2000)
month = random.randint(1, 12)
day = random.randint(1, 28)

for i in range(3):
    birth_date = datetime(year, month, day)
    my_list = {}
    my_list.append(i, str(birth_date))
    print(my_list)
