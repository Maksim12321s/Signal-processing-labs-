'''
Вариант 25
s(t) = sin(2pi * 1518 * t + 86) + sin(2pi * 3499*t + 36) + sin(2pi * 1257*t + 177)
Шум: нормальный(Гауссов)
Стандартное отклонение: 3,94

'''
import numpy as np
import sys
from pathlib import Path
def Signal(x):
    pi = np.pi
    sin1 = np.sin(2*pi * 1518 * x + 86*pi/180)
    sin2 = np.sin(2*pi * 3499 * x + 36*pi/180)
    sin3 = np.sin(2*pi * 1257 * x + 177*pi/180)

    return (sin1 + sin2 + sin3)

sig = 3.94
DIR = str(Path(__file__).parent)
START = DIR + "/signals/start.wav"
NOISE = DIR + "/signals/noise.wav"
FILTERORIG = DIR + "/signals/filter.wav"
FILTER10 = DIR + "/signals/filter10.wav"
FILTER100 = DIR + "/signals/filter100.wav"
FILTER1000 = DIR + "/signals/filter1000.wav"
N0 = 10
N1 = 100
N2 = 1000

DUR = 10
FD = 50000