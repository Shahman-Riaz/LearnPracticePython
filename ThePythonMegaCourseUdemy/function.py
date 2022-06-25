# def my_function(fname):
#     print(fname + " hello world")
# my_function("Emil")


# def my_name(name1, name2, name3):
#     print('The youngest child is ' + name3)

# my_name(name2="name2", name1="name1", name3="name3")


# def myFunction(**kid):
#     print("His last name is " + kid["lname"])

# myFunction(fname="Shahman", lname="Riaz")


# def my_country(count = "Bangladesh"):
#     print("I am from " + count)

# my_country("USA")
# my_country("UK")
# my_country()
# my_country("UAE")



# def fruits(food):
#     for x in food:
#         if x == 'cherry':
#             continue
#         print(x)
# fruits(['apple', 'banana', 'cherry', 'orange'])


## recurion of function
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)