#### Easy way to modify the elements of a list to make a new list

# temps = [221, 234, 340, 230, -999, 240]
# new_temps = [temp / 10 for temp in temps]
# print(new_temps)

# new_temps2 = [temp / 10 for temp in temps if temp != -999]
# print(new_temps2)



### if interger in list that stores integer but when any string that stores 0 to the new list.
# def seperate_int(list):
#     integer_list = [x if type(x) == int else 0 for x in list]
#     print(integer_list)

# seperate_int(["99", 22, 22.2,'3hi', 'hho', 99, 2.6])





# def sum_str(list):
#     a = 0
#     for x in list:
#        a += float(x)
#     return a
     
# sum_str(['1.2', '2.6', '3.3'])
