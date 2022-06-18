class Person:
    def __init__(self, name, age, money = 3000):
        self.name = name
        self.age = age
        self.money = money

    def myFunction(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 22)
p1.myFunction()