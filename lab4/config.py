'''
Вариант 25
𝜏 = 15 c
𝜏𝑛𝑜𝑖𝑠𝑒 = 0,08 c
𝜏0 = 10,28 c
'''
from pathlib import Path

DUR = 15
Tnoise = 0.08
T0 = 10.28

DIR = str(Path(__file__).resolve().parent)
START = DIR + "/signals/loonboon.wav"
NOISE = DIR + "/signals/loonboonNOISE.wav"
NOISE_sound = DIR + "/signals/NOISE.wav"
result = DIR + "/signals/result.wav"