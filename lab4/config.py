'''
Вариант 25
𝜏 = 15 c
𝜏𝑛𝑜𝑖𝑠𝑒 = 0,08 c
𝜏0 = 10,28 c
'''
from pathlib import Path
import numpy as np
from scipy.signal import correlate


DUR = 15
Tnoise = 2
T0 = 10.28

DIR = str(Path(__file__).resolve().parent)
START = DIR + "/signals/loonboon.wav"
NOISE = DIR + "/signals/loonboonNOISE.wav"
NOISE_sound = DIR + "/signals/NOISE.wav"
result = DIR + "/signals/result.wav"


BARKER_CODES = {
    2:  [1, -1],
    3:  [1, 1, -1],
    4:  [1, 1, -1, 1],
    5:  [1, 1, 1, -1, 1],
    7:  [1, 1, 1, -1, -1, 1, -1],
    11: [1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1],
    13: [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
}

def get_barker_code(length):
    return np.array(BARKER_CODES[length], dtype=float)

def barker_signal(length, samples_per_bit):
    code = get_barker_code(length)
    signal = np.repeat(code, samples_per_bit) 
    return signal
