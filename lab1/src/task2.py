import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

parent_path = str(Path(__file__).resolve().parent)
sys.path.insert(0, parent_path)
import config as con

def main():
    duration = con.TMAX - con.TMIN
    noise = np.random.normal(0,1,size=int(duration*con.FD))
    N = len(noise)
    window1 = np.ones(con.M1)/ con.M1
    window2 = np.ones(con.M2)/ con.M2
    window3 = np.ones(con.M3)/ con.M3

    rez1 = np.convolve(noise,window1,mode='same')
    rez1 = rez1/np.max(np.abs(rez1))

    rez2 = np.convolve(noise,window2, mode='same')
    rez2 = rez2/np.max(np.abs(rez2))

    rez3 = np.convolve(noise, window3, mode='same')
    rez3 = rez3/np.max(np.abs(rez3))


    freqs = np.fft.fftfreq(N,1/con.FD)
    freqs = freqs[:N//2]
    noisefreq = np.abs(np.fft.fft(noise)) / N
    rez1freq = np.abs(np.fft.fft(rez1)) / N
    rez2freq = np.abs(np.fft.fft(rez2)) / N
    rez3freq = np.abs(np.fft.fft(rez3)) / N

    fig, axes = plt.subplots(4,2, figsize=(20,10))
    
    t = np.linspace(con.TMIN,con.TMAX, len(noise))

    axes[0][0].plot(t,noise)
    axes[0][0].set_title("orig S(t)")

    axes[1][0].plot(t,rez1)
    axes[1][0].set_title("M = 10 S(t)")

    axes[2][0].plot(t,rez2)
    axes[2][0].set_title("M = 20 S(t)")

    axes[3][0].plot(t,rez3)
    axes[3][0].set_title("M = 33 S(t)")

    axes[0][1].plot(freqs,noisefreq[:N//2])
    axes[0][1].set_title("orig S(f)")

    axes[1][1].plot(freqs,rez1freq[:N//2])
    axes[1][1].set_title("M = 10 S(f)")

    axes[2][1].plot(freqs,rez2freq[:N//2])
    axes[2][1].set_title("M = 20 S(f)")

    axes[3][1].plot(freqs,rez3freq[:N//2])
    axes[3][1].set_title("M = 33 S(f)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()