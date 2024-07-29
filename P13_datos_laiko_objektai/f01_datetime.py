import datetime

print(type(datetime))
print(type(datetime.datetime.today()))

today = datetime.datetime.today()

# print(res)
# print(res.year)
# print(res.month)
# print(res.day)
# print(res.hour)
# print(res.minute)
# print(res.second)
# print(res.microsecond)

print("------------------")

pradzia = datetime.datetime(2000, 1, 1)
print(pradzia)

res = datetime.datetime(2011, 12, 31, 23, 59, 59)
print(res)

skirtumas_tarp_datu = today - pradzia
print(skirtumas_tarp_datu)