'''
Вариант 25
Методом гетерогинирования повысить частоту сигнала
𝑓𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙 = 4890 Гц
𝑓𝑛𝑒𝑤 = 7464 Гц
'''
import numpy as np
from pathlib import Path

DIR = str(Path(__file__).resolve().parent)
FORIG = 4890
FNEW = 7464
DUR = 5
FD = 44000

ORIG = DIR + "/signals/orig.wav"
FILTER = DIR + "/signals/filter.wav"
def Signal(x):
    return np.sin(2*np.pi*FORIG*x)

def lowpass(fd,fc,M):
    n = np.arange(M+1)
    fcn = fc/fd
    h = 2*(0.54 - 0.46 * np.sinc(2*fcn * (n - M/2)))
    h = h * (0.54 - 0.46 * np.cos(2*np.pi * n / M))
    return h/np.sum(h)

def highpass(fc, fd, M):
    h = -lowpass(fc, fd, M)
    h[M//2] += 1          
    return h