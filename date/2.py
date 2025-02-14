import datetime

x = datetime.datetime.today()
ys = x - datetime.timedelta(days = 1)
tm = x + datetime.timedelta(days = 1)


print(f" Yesterday : {ys} \n Today : {x} \n Tommorow {tm}")