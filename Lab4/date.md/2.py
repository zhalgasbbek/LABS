import datetime

x = datetime.date.today()
y = datetime.timedelta(days = 1)

print('Yesterday : ' , x - y)
print('Today : ' , x)
print('Tomorrow : ' , x + y)