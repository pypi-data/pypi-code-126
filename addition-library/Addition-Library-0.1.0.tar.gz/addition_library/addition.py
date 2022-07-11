import numpy as np


class Addition:

    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def addition(self, num1, num2):
        return np.add(num1,num2)


addition1 = Addition(10, 15)

print(addition1.addition(10, 15))
