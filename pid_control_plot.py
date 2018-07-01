#pid validation

from scipy.signal import *
import matplotlib.pyplot as plt
from dialogBlock import DialogBlock
import numpy as np

def pplot(T, yout, i):
    plt.plot(T, yout, label = f'Kp ={i}')

"""
Kp = [3, 8, 18]

for i, p in enumerate(Kp):
    
    pdig = (p*DialogBlock([1], [1, 1, 2])).cloop(True)
    pdig_tf = TransferFunction(list(pdig.num), list(pdig.den))
    T, yout = step(pdig_tf)
    pplot(T, yout, p)
    
"""

Ki = [0.5, 1, 1.5]

for count, i in enumerate(Ki):
    idig = (DialogBlock([i], [1, 0])*DialogBlock([1], [1, 1, 2])).cloop(True)
    idig_tf = TransferFunction(list(idig.num), list(idig.den))
    T, yout = step(idig_tf)
    pplot(T, yout, i)

plt.grid(True)
plt.legend()
plt.show()

