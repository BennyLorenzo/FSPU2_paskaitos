import datetime

dabar = datetime.datetime.today()
mileniumo_pradzia = datetime.datetime(2000, 1, 1)
skirtumas_tarp_datu = dabar - mileniumo_pradzia
print(type(skirtumas_tarp_datu))
print(skirtumas_tarp_datu) # 8969 days, 12:49:06.901139

res = dabar - skirtumas_tarp_datu
print(res)

laiko_skirtumas_1h = datetime.timedelta(hours=1)
res = dabar + laiko_skirtumas_1h
print(res)

res = dabar - datetime.timedelta(hours=1000)
print(res)

res = dabar + datetime.timedelta(days=1000, hours=8)
print(res)

print(skirtumas_tarp_datu)

print(skirtumas_tarp_datu.days)
print(skirtumas_tarp_datu.seconds) # tik likutis nuo dienų dalies (neapima dienų)

print(skirtumas_tarp_datu.total_seconds())