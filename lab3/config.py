'''
Вариант 25
тип фильтра: нижних частот
fc = 485
F = 1507
'''
import sys
from pathlib import Path

DIR = str(Path(__file__).resolve().parent)
START = DIR + "/signals/angry_birds.mp3"
FILTER = DIR + "/signals/filter.wav"
NOISE = DIR + "/signals/noise.wav"
FILTER_NOISE = DIR + "/signals/noise_filtered.wav"
FD = 50000
DUR = 10
FC = 485
F = 1507
M = 100