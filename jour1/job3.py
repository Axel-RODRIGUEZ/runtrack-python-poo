class Operation:
    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 2
    
    def add(self):
        self.result = self.nombre1 + self.nombre2
        return self.result

test = Operation()

print(test.add())