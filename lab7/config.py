'''
Вариант 25
Тип манипуляции: QPSK
Кодирующая последовательность:
𝐴=1011001111111101
'''
import numpy as np
from pathlib import Path

J=4
A = [1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1]
FD = 44000
PHASE={(0,0): np.pi/4, (0,1): 3*np.pi/4, (1,0): 5*np.pi/4, (1,1): 7*np.pi/4}
Fc = 2000
Tsym= 0.01


def Signal():
    ns = int(FD*Tsym)
    phases= [PHASE[(A[i],A[i+1])] for i in range(0,len(A),2)]
    phi = np.repeat(phases,ns)
    t = np.arange(len(phi)) / FD
    return (t,np.cos(2*np.pi*Fc*t + phi))