
from typing import Union
numbers = Union[float, int]
from numpy import poly1d
import scipy as sp
from scipy.signal import *
import matplotlib.pyplot as plt


class DialogBlock:
    
    def __init__(self, num, den = [1]):
        self.num = poly1d(num)
        self.den = poly1d(den)
    
    def __repr__(self) -> str:
        if len(self.den) > 0:
            return f"DialogBlock({list(self.num)} / {list(self.den)})"
        else:
            return f"DialogBlock({list(self.num)})"
    
    def __neg__(self) -> 'DialogBlock':
        return DialogBlock(-self.num, self.den)
    
    def __add__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        if type(db) == DialogBlock:
            #DialogBlock
            num_first = self.num * db.den
            num_second = self.den * db.num
            den = self.den * db.den
            num = num_first + num_second
        else:
            #Number
            num = self.num + self.den * db
            den = self.den
        return DialogBlock(num, den)
    
    def __radd__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        return self + db
    
    def __sub__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        return self + (-db)
    
    def __mul__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        if type(db) == DialogBlock:
            #DialogBlock
            num = self.num * db.num
            den = self.den * db.den
        else:
            #Number
            num = self.num * db
            den = self.den
        return DialogBlock(num, den)
    
    def __rmul__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        return self * db
    
    def __truediv__(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        if type(db) == DialogBlock:
            #DialogBlock
            num = self.num * db.den
            den = self.den * db.num
        else:
            #Number
            num = self.num
            den = self.den * db
        return DialogBlock(num, den)
    
    def series(self, db: 'DialogBlock') -> 'DialogBlock':
        return self * db
    
    def paralell(self, db: 'DialogBlock') -> 'DialogBlock':
        return self + db
    
    def feedback(self, db: Union['DialogBlock', numbers]) -> 'DialogBlock':
        if db in (1, -1):
            return self.cloop(db == 1)
        return self / (self * db + 1)
    
    def cloop(self, reversed=True) -> 'DialogBlock':
        return DialogBlock(
            self.num,
            self.num + (self.den if reversed else -self.den)
        )
"""
print((DialogBlock([2, 3], [1, 3, 1, -1])*10)
    .cloop()
)
"""
a = ((DialogBlock([2, 3], [1, 3, 1, -1])*10)
    .cloop())

c = TransferFunction(list(a.num), list(a.den))
print(c.poles.real)
print(c.zeros)
pp = []

"""
num = [1.045, 0]
den = [0.230, -0.0418, -7.171, 1.025]

num = [20, 30]
den = [1, 3, 1, -1]  #[0. +6.j 1. +7.j 2. +8.j 3. +9.j 4.+10.j]

c = TransferFunction(num, den)
m_num = [20, 30]
n_den = [1, 3, 21, 29]

T, yout = step(c)

#print(c.to_zpk())

plt.plot(T, yout, label='abs signal')


z, p, k = tf2zpk(m_num, n_den)
print(z, p, k)
a = ZerosPolesGain(z, p, k)
print(a)
plt.show()
"""
