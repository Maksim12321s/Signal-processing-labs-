'''
вариант 25
символ А
697 Гц + 1633 Гц
'''
import numpy as np
from pathlib import Path

LOW  = [697, 770, 852, 941]
HIGH = [1209, 1336, 1477, 1633]
KEYS = [['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]
F1 = 697
F2 = 1633


DUR = 10
FD = 44000
DIR = str(Path(__file__).resolve().parent)
ORIG = DIR + "/signals/orig.wav"
def Signal(x):
    return np.sin(2*np.pi*F1*x) + np.sin(2*np.pi*F2*x)


def Gerzel(x, k):
    N = len(x)
    w = 2*np.pi *k / N
    coeff = 2 * np.cos(w)

    s1 = 0
    s2 = 0

    for xn in x:
        sn = coeff* s1  - s2 + xn
        s2 = s1
        s1 = sn
    
    return np.exp(1j * w)*s1 - s2

def detect_dtmf(x, fd):
    amps_low  = [np.abs(Gerzel(x, f*len(x)/fd)) for f in LOW]
    amps_high = [np.abs(Gerzel(x, f*len(x)/fd)) for f in HIGH]
    row = int(np.argmax(amps_low))
    col = int(np.argmax(amps_high))
    return KEYS[row][col], LOW[row], HIGH[col], amps_low, amps_high