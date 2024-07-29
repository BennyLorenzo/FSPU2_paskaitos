import datetime

res = datetime.datetime(1999, 11, 2, 10, 10)
print(res)

ivestis = "1999 11 2"

res = datetime.datetime.strptime(ivestis, "%Y %m %d")
print(res)

ivestis = "1999 11 2, 10:15:30"

res = datetime.datetime.strptime(ivestis, "%Y %m %d, %I:%M:%S")
print(res)

print(res.strftime("%d %B, %Y"))
