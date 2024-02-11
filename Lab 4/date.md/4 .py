import datetime

x = datetime.datetime(2018, 6, 1 , 6 , 15 , 22)
y = datetime.datetime(2018, 6, 1 , 6 , 11 , 23)

z = x - y
print(x.second - y.second)

print(int(x.strftime("%S")) - int(y.strftime("%S")))

print(z.seconds)

differenceinseconds = z.total_seconds()
print( differenceinseconds)