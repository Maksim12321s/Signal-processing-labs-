import numpy as np
import wave
from scipy.io import wavfile



def generateSignalarray(signal,FD, duration):
    N = int(FD*duration)
    a = np.linspace(0, duration, N)
    y = signal(a)
    norm = y/np.max(np.abs(y))
    return norm

def generateSignalintoFile(data,FD, file):
    dataToWrite = np.int16(data*32767)
    with wave.open(file,"w") as wav:
        wav.setparams((1,2,FD, 0, 'NONE', 'not compressed'))
        wav.writeframes(dataToWrite.tobytes())

def readFromFile(file):
    FD, data = wavfile.read(file)
    return FD, data