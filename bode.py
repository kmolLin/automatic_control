#bode use

import numpy as np
from dialogBlock import DialogBlock
import matplotlib.pyplot as plt

def bode(num, den):
    f = np.logspace(-2, 4, 1000)
    w = 2*np.pi*f
    s = 1.0j*w
    Gjw = (num(s))/(den(s))
    db_mag = 20*np.log10(np.abs(Gjw))

    phase = np.arctan2(np.imag(Gjw), np.real(Gjw))*180/np.pi
    
    plt.figure()
    plt.subplot(211)
    plt.semilogx(f, db_mag)
    plt.ylabel('dB Mag')
    plt.subplot(212)
    plt.semilogx(f, phase)
    plt.xlabel('Freq (Hz)')
    plt.ylabel('Phase (deg)')
    plt.show()
        
'''
f = np.logspace(-2, 4, 1000)

w = 2*np.pi*f
s = 1.0j*w

p1 = 1.0*2*np.pi
p2 = 100.0*2*np.pi

tf = DialogBlock([p1*p2], [1, p1+p2, p1*p2])

Gjw = (tf.num(s))/(tf.den(s))

db_mag = 20*np.log10(np.abs(Gjw))

phase = np.arctan2(np.imag(Gjw), np.real(Gjw))*180/np.pi

plt.figure()
plt.subplot(211)
plt.semilogx(f, db_mag)
plt.ylabel('dB Mag')
plt.subplot(212)
plt.semilogx(f, phase)
plt.xlabel('Freq (Hz)')
plt.ylabel('Phase (deg)')

plt.show()
'''
