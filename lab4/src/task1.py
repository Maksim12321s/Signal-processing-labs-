import sys
from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

parent = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0,parent)

import lab1.scripts.generate as gen
import lab4.config as con



def SubTask1():
    fd, data = gen.readFromFile(con.START)
    data = data.mean(axis=1)
    data = data /  np.max(np.abs(data))

    N = len(data)
    duration = N*fd

    t = np.linspace(0, duration, N)
    freqs = np.fft.fftfreq(N, 1/fd)

    spectr = np.abs(np.fft.fft(data)) / N
    spectr[0] = 0

    fig, axes = plt.subplots(2,1, figsize=(12,8))

    axes[0].plot(t, data)
    axes[0].grid(True)
    axes[1].plot(freqs[:N//2],spectr[:N//2])
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def SubTask2():
    fd, data = gen.readFromFile(con.START)
    data = data.mean(axis=1)
    data = data/np.max(np.abs(data))
    orig = data.copy()
    N = len(data)
    noise = np.random.normal(0,1,int(con.Tnoise * fd))
    noise = noise / np.max(np.abs(noise))
    ind = int(con.T0 * fd)
    end_ind = int(ind + con.Tnoise*fd)


    data[ind: end_ind] += noise
    # data = data / np.max(np.abs(data))

    gen.generateSignalintoFile(data,fd,con.NOISE)
    gen.generateSignalintoFile(noise,fd,con.NOISE_sound)

    t = np.linspace(0, con.DUR, N)
    freqs = np.fft.fftfreq(N, 1/fd)
    spectr = np.abs(np.fft.fft(data)) / N
    spectr_orig = np.abs(np.fft.fft(orig))/N

    fig, axes = plt.subplots(2,3, figsize=(12,8))

    axes[1][0].plot(t,data)
    axes[1][1].plot(freqs[:N//2], spectr[:N//2])

    axes[0][0].plot(t,orig)
    axes[0][1].plot(freqs[:N//2],spectr_orig[:N//2])

    rez = np.abs(spectr - spectr_orig)
    axes[0][2].plot(t, data - orig)

    f, t_spec, Sxx = spectrogram(data, fd, nperseg=1024)

    axes[1][2].pcolormesh(t_spec, f, 10*np.log10(Sxx + 1e-12), shading='auto')
    plt.tight_layout()
    plt.show()

def SubTask3():
    fd, data = gen.readFromFile(con.NOISE)
    fd, noise = gen.readFromFile(con.NOISE_sound)

    data = data/np.max(np.abs(data))
    noise = noise/np.max(np.abs(noise))

    N = len(data)
    h = noise[::-1]
    y = np.convolve(data,h,mode='same')

    peak_ind = np.argmax(np.abs(y))
    peak_time = peak_ind / fd

    t = np.linspace(0,con.DUR, N)

    fig, axes = plt.subplots(2,1, figsize=(12,8))

    axes[0].plot(t,data)
    axes[0].grid(True)

    axes[1].plot(t,y)
    axes[1].grid(True)
    y = y/np.max(np.abs(y))
    # gen.generateSignalintoFile(y,fd,con.result)
    plt.tight_layout()
    plt.show()



def main():
    SubTask3()


if __name__ == "__main__":
    main()