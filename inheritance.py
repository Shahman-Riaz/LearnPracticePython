# class Person:
#     def __init__(fack, fname, lname):
#         fack.firstname = fname
#         fack.lastname = lname
    
#     def printname(chutiya):
#         print(chutiya.firstname, chutiya.lastname, chutiya.graduationyear)

# class Student(Person):
#     def __init__(fack, fname, lname, year):
#         super().__init__(fname, lname)
#         fack.graduationyear = year

# x = Student("Mike", "Olsen", 2319)
# print(x.graduationyear)











class Computer:
    def __init__(self, casing, monitor = "HP"):
        self.pc = casing
        self.monitor = monitor

    def overview(self):
        print(self.pc, self.monitor, "are the outlook of a computer")

class Cpu(Computer):
    def __init__(self, casing, ram, ssd, motherboard, monitor="HP" ):
        super().__init__(casing, monitor)
        self.ram = ram
        self.motherboard = motherboard
        self.ssd = ssd

    def configuration(self):
        print("Configuration: ", self.pc, self.ram, self.ssd, self.monitor, self.motherboard)

x = Cpu("Delux", "8GB", "250GB", "Gigabyte")
x.configuration()
