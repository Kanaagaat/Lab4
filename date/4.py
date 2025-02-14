import datetime

x = datetime.datetime(2022, 7,15)
y = datetime.datetime.today()

dif = y - x

print(dif.total_seconds())