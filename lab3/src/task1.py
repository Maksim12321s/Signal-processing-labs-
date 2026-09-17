import sys
from pathlib import Path
import librosa
import numpy as np
import matplotlib.pyplot as plt
import argparse




parent_path = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0,parent_path)


import lab1.scripts.generate as gen
import lab3.config as con

def SubTask1():
    print(con.START)
    data, fd = librosa.load(con.START)
    data /= np.max(np.abs(data))
    N = len(data)
    duration = N / fd
    t = np.linspace(0, duration, N)
    
    spectr = np.abs(np.fft.fft(data))/ N
    freqs = np.fft.fftfreq(N, 1/fd)
    spectr[0] = 0

    fig, axes = plt.subplots(2,1,figsize=(12,8))

    axes[0].plot(t, data)

    axes[1].plot(freqs[:N//2], spectr[:N//2])

    plt.tight_layout()
    plt.show()

def SubTask2():
    data,fd = librosa.load(con.START)
    n = np.arange(con.M + 1)
    fc_norm = con.FC/fd
    h = 2 * fc_norm * np.sinc(2 * fc_norm * (n - con.M/2))
    window = 0.54 - 0.46 * np.cos(2*np.pi * n / con.M)

    h = h*window
    h = h/np.sum(h)

    N = len(data)
    duration = N/fd
    filter = np.convolve(data,h,mode='same')

    freq = np.fft.fftfreq(N, 1/fd)
    spectr = np.abs(np.fft.fft(filter)) / N
    spectr[0] = 0
    t = np.linspace(0, duration, N)

    fig, axes = plt.subplots(2,1,figsize=(12,8))

    axes[0].plot(t, filter)

    axes[1].plot(freq[:N//2], spectr[:N//2])

    gen.generateSignalintoFile(filter, fd, con.FILTER)
    plt.tight_layout()
    plt.show()

def SubTask3():
    N = con.DUR * con.FD
    noise = np.random.normal(0,1, N)
    noise /= np.max(np.abs(noise))
    n = np.arange(con.M + 1)
    fc_norm = con.F/con.FD
    h = 2 * fc_norm * np.sinc(2 * fc_norm * (n - con.M/2))
    window = 0.54 - 0.46 * np.cos(2*np.pi * n / con.M)

    h = h*window
    h = h/np.sum(h)

    filter = np.convolve(noise,h,mode='same')

    t = np.linspace(0, con.DUR, N)
    
    freqs = np.fft.fftfreq(N, 1/con.FD)
    freqs = freqs[:N//2]
    spectr = np.abs(np.fft.fft(noise)) / N
    filt_spectr = np.abs(np.fft.fft(filter)) / N

    fig, axes = plt.subplots(2,2, figsize=(12,8))

    axes[0][0].plot(t,noise)
    axes[0][1].plot(freqs, spectr[:N//2])

    axes[1][0].plot(t,filter)
    axes[1][1].plot(freqs,filt_spectr[:N//2])
    # gen.generateSignalintoFile(noise,con.FD, con.NOISE)
    # gen.generateSignalintoFile(filt_spectr, con.FD, con.FILTER_NOISE)
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="выберите номер задания")
    parser.add_argument("--mode",
                        choices=["orig","filter", "noise"],
                        required=True)
    args = parser.parse_args()
    if args.mode == "orig":
        SubTask1()
    elif args.mode == "filter":    
        SubTask2()
    elif args.mode == "noise":
        SubTask3()



if __name__ == "__main__":
    main()