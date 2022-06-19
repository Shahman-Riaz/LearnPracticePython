# i = 100
# while (i > 10):
#     print(i)
#     i -= 10
    

# data = 'python'
# i = 0
# while (i < len(data)):
#     print(data[i])
#     i += 1


# data = 'I love data science'
# data = data.split()
# i = 0
# while (i < len(data)):
#     print(data[i])
#     i += 1



### turn the loop while the sum of the taken numbers is less than 11
# sum = 0
# while sum < 11:
#     num = int(input("Enter a number: "))
#     sum += num
# print(sum)




# a = 0
# while a < 5:
#     a = a + 1
#     print(a)


names = []
while True:
    userName = input("Enter username: ")
    names.append(userName)
    if userName == "pypy":
        break
    elif len(names) == 5:
        break
    else:
        continue