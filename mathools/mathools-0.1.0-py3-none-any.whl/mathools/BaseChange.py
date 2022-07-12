import numpy as np
from math import log

class Base():
    
    def __init__(self, base: int, *, symbols: np.ndarray = None) -> None:
        self.base  = base
        
        if symbols == None:
            sym = [i for i in range(10)]
            sym += [chr(i) for i in range(65, 91)]
            symbols = np.array(sym, dtype=str)
        self.symbols = symbols
        
        if self.base > len(self.symbols):
            raise ValueError(f"Not enough symbols (number of symbols: {len(self.symbols)}) for the base {self.base}")
    
    def _factor(self, v: float) -> tuple:
        order = int(np.floor(log(v, self.base)))
        orders = range(0, order+1)[::-1]
        
        digits = np.empty((order+1), dtype=int)
        for place in orders:
            digit = int(np.floor(v / self.base**place))
            digits[place] = digit
            v = v % (self.base**place)
        
        return digits, orders
    
    def convert_value(self, v: float) -> str:
        digits, orders = self._factor(v)
        return "".join([self.symbols[digits[i]] for i in orders])

if __name__ == "__main__":
    b16 = Base(16)
    print(b16.convert_value(128))