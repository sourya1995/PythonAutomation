import math


class Shape:
    def __init__(self, name):
        self.name = name
    def perimeter(self):
        raise NotImplementedError("perimeter")
    def area(self):
        raise NotImplementedError("area")
    def density(self, weight):
        return weight / self.area()
    
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    def perimeter(self):
        return self.side * 4
    def area(self):
        return self.side * self.side
    
    
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius * self.radius
    
examples = [Square('square', 5), Circle('circle', 5)]
for thing in examples:
    n = thing.perimeter
    d = thing.density(5)
    print(f"{n}: {d:.2f}")

# def square_perimeter(thing):
#     return 4 * thing["side"]

# def square_area(thing):
#     return thing["side"] * thing["side"]

# def square_new(name, side):
#     return {
#         "name": name,
#         "side": side,
#         "perimeter": square_perimeter,
#         "area": square_area
#     }

