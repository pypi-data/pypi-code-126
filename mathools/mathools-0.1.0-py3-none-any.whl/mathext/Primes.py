from xml.dom import ValidationErr
import numpy as np

class _Primes():
    
    def __init__(self) -> None:
        self.max_num_elements = 1e7
        self.primes = np.array([2, 3, 5])
        self.limit = np.inf
        self._update_min_max()
        
    def _update_min_max(self) -> None:
        self.min_ = self.primes[-1]
        self.max_ = self.min_ ** 2
        if self.min_ + self.max_num_elements < self.max_:
            self.max_ = self.min_ + self.max_num_elements
        if self.max_ > self.limit:
            self.max_ = self.limit
        self.min_ = int(self.min_)
        self.max_ = int(self.max_)
    
    def _next_batch(self) -> None:
        self._update_min_max()
        
        candidates = np.ones(self.max_ - self.min_, dtype=bool)
        
        for prime in self.primes:
            start = (prime - self.min_%prime)%prime
            candidates[start::prime] = False
        
        new_primes = candidates.nonzero()[0] + self.min_
        self.primes = np.append(self.primes, new_primes)
    
    def between(self, lower: int, upper: int) -> np.ndarray:
        self.limit = upper + 1
        while self.primes[-1] < upper and self.max_ < self.limit:
            print(f"{self.max_ / upper * 100 : 6.2f}%", end='\r')
            self._next_batch()
        print(7*" ", end="\r")
        
        idx_l = self.primes.searchsorted(lower, side='left')
        
        if self.primes[-1] > upper:
            idx_u = self.primes.searchsorted(upper+1, side='left')
            return self.primes[idx_l:idx_u]
        return self.primes
    
    def factor(self, num: int) -> np.ndarray:
        self.between(0, num)
        num_ = num
        factor = []
        for prime in self.primes:
            while num%prime == 0:
                factor.append(prime)
                num /= prime
            if num == 1:
                break
        if not np.prod(factor) == num_:
            raise ValidationErr(f"The product of {factor} is {np.prod(factor)} but should be {num_}")
        return np.array(factor, dtype=int)
    
    def closest_prime(self, num: float) -> int:
        self.between(0, 2*num)
        idx = self.primes.searchsorted(num, side='left')
        if num - self.primes[idx-1] <= self.primes[idx] - num:
            return self.primes[idx-1]
        return self.primes[idx]

primes = _Primes()
 
if __name__ == "__main__":    
    n = 1e6
    c = primes.closest_prime(n)
    print(c)
    f = primes.factor(n)
    print(f)