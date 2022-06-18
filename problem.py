# ages = []
# i = 0
# while i<3:
#    age = int(input("Enter age: "))
#    ages.append(age)
#    i+=1
# for x in ages:
#     if x < 16:
#         print("Too young!")
#         break
# else:
#         print("Get ready!")
        
        


# def concatenate(*args):
#         return '-'.join(args)
# print(concatenate("I", "love", "Python", "!"))


txt = input()
text_list = txt.split(" ")
longest_word = ""

for x in text_list:
        if (len(x) > len(longest_word)):
                longest_word = x
print(longest_word)

