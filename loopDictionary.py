# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.7}

# for name, grade in student_grades.items():
#     print(f'{name} got {grade}')



name_dict = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for name, phoneNumber in name_dict.items():
    print(f'{name}: {phoneNumber}')
    print(phoneNumber.replace("+", "00"))