class Calculator:
    def __init__(self,num):
        self.number = num
        
    def square(self):
        print(f"The value of{self.num} square is {self.num **2}")

    def squareroot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")

a = Calculator(7)
a.square()
a.squareroot()
