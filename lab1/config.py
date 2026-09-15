"""
Вариант 25:
    s(t) = sin(2*pi*6345*t + 203°)
    f0 = 6590 Гц, fn = 8395 Гц
    M1 = 10, M2 = 20, M3 = 33
"""

import numpy as np

START_sig = "signals/start_signal.wav"
NOISE = "signals/noise.wav"
WINDOW = "signals/window.wav"
def Signal(x):
    return np.sin(2*np.pi*6345*x + 203*np.pi/180)

FD = 30000
F0 = 6383
Fn = 8395

TMIN = 0
TMAX = 10


M0 = 31
M1 = 10
M2 = 20
M3 = 33
