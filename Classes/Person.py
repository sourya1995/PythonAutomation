class Person:
    def __init__(self, name, age): #class constructor
        self.name = name #class variable
        self.age = age #class variable

    def greet(self):
        print(f"Hello, {self.name}")

class TenYearOldPerson(Person):
    def __init__(self, name):
        Person.__init__(self, name, 10)

    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old")


a = Person("Anna", 20)
b = Person("Bob", 21)
a.greet()
b.greet()

child = TenYearOldPerson("John")
child.greet()