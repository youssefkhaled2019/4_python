import datetime
from datetime import date
import time


x = datetime.datetime.now()# 2025-03-25 06:07:59.616665 

print(x)
print(x.year)
print(x.strftime("%A")) 

#==============create a date======[datetime]===========
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
#  but they are optional, and has a default value of 0, (None for timezone).
x = datetime.datetime(2020, 5, 17)#2020-05-17 00:00:00
print(x.strftime("%B"))

#------------

# a = datetime(year=2011, month=3, day=15,hour=13 ,minute = 15, second = 9)
# b = datetime(year=1982, month=2, day=2,hour=18 ,minute = 43, second = 12)
# print(a) #2011-03-15 13:15:09
# print(b) #1982-02-02 18:43:12
# print(a-b) # 10632 days, 18:31:57

#=============[date]==================

# now = date.today() #2025-04-01
# a = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(a)  #04-01-25. 01 Apr 2025 is a Tuesday on the 01 day of April.
#------------
# a = date(1982, 2, 2)
# print(a) #1982-02-02
#------------

# now = date.today()
# a = date(1997, 3, 11)
# z = now-a
# print(z) 9418 days, 0:00:00
#------------

# a = date(1982, 2, 2)
# b = date(2011, 3, 15)
# z = b-a
# print(z) #10633 days, 0:00:00

#=====================[time]=====================

# t = time.gmtime()
# print(t) #time.struct_time(tm_year=2022, tm_mon=12, tm_mday=23, tm_hour=9, tm_min=33, tm_sec=19, tm_wday=4, tm_yday=357, tm_isdst=0)
#------------
# def wait(x):
#  t0 = time.time()
#  while time.time() - t0 < x:
#    time.sleep(1)
#  return x

# print('start')
# wait(3)
# print('finish')
#------------

#=================reference of all the legal format================
# Directive 	Description 	                                                Example 	Try it
# %a 	        Weekday, short version                  	                    Wed 	
# %A 	        Weekday, full version 	                                        Wednesday 	
# %w 	        Weekday as a number 0-6, 0 is Sunday 	                        3 	
# %d 	        Day of month 01-31 	                                            31 	
# %b 	        Month name, short version 	                                    Dec 	
# %B 	        Month name, full version 	                                    December 	
# %m 	        Month as a number 01-12 	                                    12 	
# %y 	        Year, short version, without century 	                        18 	
# %Y 	        Year, full version 	                                            2018 	
# %H 	        Hour 00-23 	                                                    17 	
# %I 	        Hour 00-12 	                                                    05 	
# %p 	        AM/PM 	                                                        PM 	
# %M 	        Minute 00-59 	                                                41 	
# %S 	        Second 00-59 	                                                08 	
# %f 	        Microsecond 000000-999999 	                                    548513 	
# %z 	        UTC offset 	                                                    +0100 	
# %Z 	        Timezone 	                                                    CST 	
# %j 	        Day number of year 001-366              	                    365 	
# %U 	        Week number of year, Sunday as the first day of week, 00-53 	52 	
# %W 	        Week number of year, Monday as the first day of week, 00-53 	52 	
# %c 	        Local version of date and time 	                                Mon Dec 31 17:41:00 2018 	
# %C 	        Century 	                                                    20 	
# %x 	        Local version of date 	                                        12/31/18 	
# %X 	        Local version of time 	                                        17:41:00 	
## %% 	        A % character 	                                                % 	
# %G 	        ISO 8601 year 	                                                2018 	
# %u 	        ISO 8601 weekday (1-7) 	                                        1 	
# %V 	        ISO 8601 weeknumber (01-53) 	                                01


        # %%