# import mymodule as mm

# a = mm.person1["age"]
# print(a)


# import platform
# x = platform.system()
# y = dir(platform)
# print(y)



import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().strftime("%B")
day = datetime.datetime.now().strftime("%A")
# z = datetime.datetime(2020, 5, 17)
# print(z.strftime("%B"))
print(year, month, day)

