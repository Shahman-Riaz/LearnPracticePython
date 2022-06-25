# def myFunction(n):
#     return lambda a : a * n

# x = lambda a : a * 3
# print(x(5))


# def myfunction(n):
#     return lambda a : a * n
# mydoubler = myfunction(3)
# print(mydoubler(5))






def myNumber(n):
    return lambda a : a * n
mydoubler = myNumber(2)
mytripler = myNumber(3)

print(mydoubler(20))
print(mytripler(20))

