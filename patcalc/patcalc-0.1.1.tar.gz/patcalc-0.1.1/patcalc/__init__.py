""" Calculate basic operations from value inside the
    calculator's memory """

import math
from typing import Optional

__version__ = "0.1.1"

__all__ = ["Calculator"]


class Calculator:
    """
    Calculate basic operations from value inside the
    calculator's memory.

    Instance methods takes only int/floats as arguments.

    * Calculator().add(n)  >> Addition to memory's value
    * Calculator().subs(n) >> Substraction to memory's value
    * Calculator().mult(n) >> Multiplication to memory's value
    * Calculator().div(n)  >> Division to memory's value
    * Calculator.root()    >> Take () root of memory's value
    * Calculator().root(n) >> Sets memory to 0 and Take (n)root
    * Calculator().reset() >> Resets memory to 0.0

    >>> c = Calculator() # instance sets memory to 0
    >>> c.add(2) # add 2 to the memory value
    2.0
    >>> c.subs(-1)
    3.0
    >>> c.subs(2)
    1.0
    >>> c.mult(3)
    3.0
    >>> c.div(3)
    1.0
    >>> c.root()
    1.0
    >>> c.root(25)
    5.0
    >>> c.add(20)
    25.0
    >>> c.reset()
    0.0
"""

    memory: float = 0.0
    number: float

    def __init__(self) -> None:
        """ Initiates class and sets up memory to 0 """
        self.memory: float = 0.0

    def add(self, number: float) -> float:
        """ Add a number to the current memory """
        self.memory += number
        return self.memory

    def subs(self, number: float) -> float:
        """ Substract a number from the current memory """
        self.memory -= number
        return self.memory

    def mult(self, number: float) -> float:
        """ Miltiply a number to the current memory """
        self.memory *= number
        return self.memory

    def div(self, number: float) -> float:
        """ Divide a number to the current memory """
        self.memory /= number
        return self.memory

    def root(self, number: Optional[float] = None) -> float:
        """ Calculate the root of the current memory """
        if number:
            self.memory = math.sqrt(float(number))
            return self.memory
        number = self.memory
        self.memory = math.sqrt(number)
        return self.memory

    def reset(self) -> float:
        """ Reset memory to 0 """
        self.memory = 0.0
        return self.memory


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

