

from scipy.signal import *
import matplotlib.pyplot as plt
from dialogBlock import DialogBlock
import numpy as np
from root_locus import compute_roots, plot_root_locus
from bode import bode

def polezeroMap(zeropoints, polepoints):
    fig,ax = plt.subplots()
    ax.plot(zeropoints.real,zeropoints.imag, 'g^', label = 'zero points')
    ax.plot(polepoints.real,polepoints.imag, 'ro', label = 'polepoints')
    ax.legend(loc='best')
    

def ord2(Wn, zeta):
    return DialogBlock([Wn*Wn], [1, 2*Wn*zeta, Wn*Wn])

a = ((DialogBlock([10, 20], [1, 50, 0])))

bode(a.num, a.den)

gains = np.linspace(0.0, 1000.0, num=500)

#a = (DialogBlock([1, 2], [1, 2, 3, 0]).cloop())

c = TransferFunction(list(a.num), list(a.den))

#plot_root_locus(gains, compute_roots(a, gains))

t = np.linspace(0, 10)
u = np.ones_like(t)
r = t
tout, y, x = lsim(c, r, t)

print(r[49]-y[49])
#print(c.zeros.real)

print(ord2(5, 0.6))
seco = ord2(5, 0.6)
secondorder = TransferFunction(list(seco.num), list(seco.den))
w, H = freqresp(c)

#T, yout = step(secondorder)
#plt.plot(H.real, H.imag, "b")
#plt.plot(H.real, -H.imag, "r")
#plt.show()
"""
plt.plot(T, yout)
plt.plot(t, y, label='abs signal')
plt.plot(t, r)
"""
pp = []

#polezeroMap(c.poles, c.zeros)


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
