class MyRange:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration
        

for value in MyRange(1, 5):
    print(value)