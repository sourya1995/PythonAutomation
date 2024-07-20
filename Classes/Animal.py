class Animal ():
    def __init__(self, name, food, characteristic):
        self.name = name
        self.food = food
        self.characteristic = characteristic
    def printer(self):
        print(f"I am a  {self.name}")

class Mammal(Animal):
    def __init__(self, name, food):
        Animal.__init__(self,name, food, "warm blooded")
    def printer(self):
        print("I am a warm blooded")

class Carnivore(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
    def printer(self):
        print("I eat meat")



lion = Carnivore("lion")
lion.printer()