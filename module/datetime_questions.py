import datetime
from datetime import timedelta

now=datetime.datetime.now()
string_date_now=str(now)
print(now)

# tod=datetime.datetime.today()
# print(tod)


# today_date=datetime.date(2025,12,19)
# print(today_date)
# print(today_date.day)
# print(today_date.year)
# print(today_date.month)


# date_time=datetime.time(14,30,45)
# print(date_time)

# date_now="2025-10-03 14:57:05"
# dt_obj=datetime.datetime.strptime(date_now,"%A, %d %B %Y %I:%M %p")

# print(dt_obj)

# dt_str = "2025-10-03 14:30:45"
# dt_obj = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
# print(dt_obj)



# date_now="2025-10-03 15:16:35"

# date_obj=datetime.datetime.strptime(date_now,"%Y-%m-%d %H:%M:%S")

# print(date_obj)

# mydate=datetime.datetime( 2025,10,3,14,16,35)
# mydatetime=mydate.strftime("%A,%d,%B,%Y,%I,%M,%p" )
# print(mydatetime)

# myday=datetime.datetime.now()
# mydateview=myday.strftime("%B")
# print(mydateview)


today=datetime.date.today()

# yesterday=today -timedelta(days=1)
# tommrow=today +timedelta(days=1)

# print(f"The date before {today} is {yesterday}")
# print(f"The date after {today} is {tommrow}")
# # print(today)

mydatetime=datetime.date(2025,12,19)
delta=mydatetime-today
print(delta.days)


utc_zone=datetime.datetime.utcnow()
print(utc_zone)