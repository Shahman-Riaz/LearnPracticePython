# user_input = input("Enter your name: ")
# message = "Hello, %s!" % user_input
# print(message)



####string formating for Muliple variables"
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# age = 23
# brothers = int(input("Enter the number of your brothers: "))
# print("%s is %d years old and %s has %d brothers" %(fname, age, lname, brothers))

# print(f"{fname} is {age} years old and {lname} has {brothers} brothers too")


colors = [11, 24.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color) == int:
        print(color)