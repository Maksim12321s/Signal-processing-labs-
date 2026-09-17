import sys
from pathlib import Path
import argparse

parent_path = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, parent_path)

import matplotlib.pyplot as plt
import numpy as np

import config as con
import lab1.scripts.generate as gen

def SubTask1():
    N = con.DUR * con.FD
    t = np.linspace(0,con.DUR,N)
    signal = con.Signal(t)
    signal = signal / np.max(np.abs(signal))
    spectr = np.abs(np.fft.fft(signal)) / N
    freqs = np.fft.fftfreq(N,1/con.FD)
    freqs = freqs[:N//2]
    spectr = spectr[:N//2]
    fig, axes = plt.subplots(1,2,figsize=(12,5))

    axes[0].plot(t,signal)
    axes[0].set_title("S(t) orig")
    axes[0].set_xlabel("t, s")
    axes[0].set_ylabel("A")
    axes[0].grid(True)

    axes[1].plot(freqs,spectr)
    axes[1].set_title("S(f) orig")
    axes[1].set_xlabel("f, Hz")
    axes[1].set_ylabel("A")
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()

    gen.generateSignalintoFile(signal,con.FD,con.START)
    print("file with signal generated")

def SubTask2():
    N = con.FD * con.DUR
    noise = np.random.normal(0,con.sig, N)
    FD, data = gen.readFromFile(con.START)
    data = data/np.max(np.abs(data))

    signal_power = np.mean(np.abs(data)**2)
    noise_power = np.mean(np.abs(data)**2)

    noise = noise * np.sqrt(signal_power/noise_power)
    data += noise
    data = data/ np.max(np.abs(data))

    t = np.linspace(0,con.DUR, N)
    freq = np.fft.fftfreq(N, 1/con.FD)
    freq = freq[:N//2]
    spectr = np.abs(np.fft.fft(data))/N
    fig, axes = plt.subplots(1,2,figsize=(12,8))

    axes[0].plot(t,data)
    axes[0].set_title("S(t) with noise")
    axes[0].set_xlabel("t, s")
    axes[0].set_ylabel("A")
    axes[0].grid(True)


    axes[1].plot(freq,spectr[:N//2])
    axes[1].set_title("S(f) with noise")
    axes[1].set_xlabel("f, Hz")
    axes[1].set_ylabel("A")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

    gen.generateSignalintoFile(data,con.FD, con.NOISE)
    print("file with noise generated")

def SubTask3():
    fd, data = gen.readFromFile(con.START)
    data = data/np.max(np.abs(data))
    N = len(data)
    acc1 = np.zeros(N)
    acc2 = np.zeros(N)
    acc3 = np.zeros(N)
    for _ in range(con.N0):
        noise = np.random.normal(0,con.sig,N)
        acc1 += (data +  noise)
    acc1 /= con.N0
    for _ in range(con.N1):
        noise = np.random.normal(0,con.sig,N)
        acc2 += (data + noise)
    acc2 /= con.N1
    for _ in range(con.N2):
        noise = np.random.normal(0,con.sig, N)
        acc3 += (data + noise)
    acc3 /= con.N2

    acc1 /= np.max(np.abs(acc1))
    acc2 /= np.max(np.abs(acc2))
    acc3 /= np.max(np.abs(acc3))
    freq = np.fft.fftfreq(N, 1/con.FD)
    t = np.linspace(0, con.DUR, N)
    spec1 = np.abs(np.fft.fft(acc1)) / N
    spec2 = np.abs(np.fft.fft(acc2)) / N 
    spec3 = np.abs(np.fft.fft(acc3)) / N

    fig, axes = plt.subplots(3,3,figsize=(15,12))

    axes[0][0].plot(t, acc1)
    axes[1][0].plot(t, acc2)
    axes[2][0].plot(t, acc3)
    axes[0][1].plot(freq[:N//2], spec1[:N//2])
    axes[1][1].plot(freq[:N//2], spec2[:N//2])
    axes[2][1].plot(freq[:N//2], spec3[:N//2])
    axes[0][2].plot(t,data)

    axes[0][2].set_title("clean signal")

    plt.tight_layout()
    plt.show()

    gen.generateSignalintoFile(data,fd,con.FILTERORIG)
    gen.generateSignalintoFile(acc1,fd,con.FILTER10)
    gen.generateSignalintoFile(acc2,fd,con.FILTER100)
    gen.generateSignalintoFile(acc3,fd,con.FILTER1000)
    print("All signals generated")

def main():
    parser = argparse.ArgumentParser(description="номер задания")
    parser.add_argument("--mode",
                        choices=["orig","noise", "filter"],
                        required=True,
                        help="выберите задание, которое хотите отобразить")
    args = parser.parse_args()
    if args.mode == "orig":
        SubTask1()
    elif args.mode == "noise":
        SubTask2()
    elif args.mode == "filter":
        SubTask3()

if __name__ == "__main__":
    main()
