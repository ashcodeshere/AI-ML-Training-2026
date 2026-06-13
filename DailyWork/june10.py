# Module - 
# Package - 
# Created package - Mypackage
# to Import Packages/Module - 
# from {PackageName/ModuleName} import {ModuleName/FunctionName}
# import {PackageName/ModuleName}
# import {PackageName/ModuleName} as p
# Random Module
# - Random -> 0 to 1 (float values)
# - Random INT -> Integer Values between Range
# - RandRange 
# shuffle, choice, choices, sample, seed, randint, random, uniform
# Date Time Module
# from datetime import datetime,date
# print(datetime.now())
# print(datetime.today())
# print(date.fromisocalendar(2026,50,2))
# Year, Month, Day, Hour, Minute, second
# UTC-Coordinated Universal Time - import pytz(Python Time Zone)

# re 
# random 

# date and time 

# get current date 
# import date_time 
# from datetime import datetime,date

# print(time.time())
# print(datetime.today())

# now=datetime.now()
# print("current time: ",now)
# print(type(now))


# current_date=now.date()
# print(current_date)
# print(type(current_date))
# current_time=now.time()
# print(current_time)
# # print(type(current_time))


# print(now.year)
# print(now.month)
# print(now.day)

# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)



# today=date.today()
# print(today)

# import time 
# t=time.time()
# print(t)

# print(time.ctime(time.time()))
# t=time.localtime(time.time())
# print(t)


# datetime 
# get current time and date 
# import datetime module 
# current date 
# current time 
# from datetime import datetime 
# now =datetime.now()
# print(now)
# cd=(datetime.now()).date()
# print(cd)
# ct=now.time()
# print(ct)
# print("year: ",now.year)
# print("month: ",now.month)
# print("day: ",now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# from datetime import date 
# today=date.today()
# print(today)

# import time 
# t=time.time()
# print(t)
# print(time.ctime())
# local time 
# t=time.localtime(time.time())
# print(t)

# ms=int(t*1000)
# print(ms)

# utc time:- coordinated universal time 
# from datetime import datetime , timezone 
# tz=datetime.now(timezone.utc)
# print(tz)


# get current time in a specific timezone 
# pytz

# from datetime import datetime 
# import pytz 
# dt_us_central=datetime.now(pytz.timezone('US/Central'))
# print(dt_us_central.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
# print(dt_us_central.tzname)
