import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
from pathlib import Path

parent_path = str(Path(__file__).resolve().parent)
sys.path.insert(0, parent_path)
import config as con
import scripts.generate as gen

def SubTask1():
    duration = con.TMAX - con.TMIN
    gen.generateSignalintoFile(gen.generateSignalarray(con.Signal,con.FD,duration),con.FD,con.START_sig)


def SubTask2():
    fd, data = gen.readFromFile(con.START_sig)
    data = data.astype(np.float64) / 32767
    N = len(data)

    t = np.linspace(0, N/fd, N)

    spectr = np.fft.fft(data)
    freqs = np.fft.fftfreq(N,d = 1/fd)
    freqs_pos = freqs[:N//2]
    magnitude = np.abs(spectr[:N//2])/N

    fig,axes = plt.subplots(2,1,figsize=(12,8))

    #1
    axes[0].plot(t,data)
    axes[0].set_title("S(t)")
    axes[0].set_xlabel("Time, s")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)

    #2
    axes[1].plot(freqs_pos,magnitude)
    axes[1].set_title("S(f)")
    axes[1].set_xlabel("Freq, Hz")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def SubTask3():

    fd, data = gen.readFromFile(con.START_sig)
    data = data/np.max(np.abs(data)) 
    N = len(data)

    noise = np.random.normal(0,1,size=N)
    spectr = np.fft.fft(noise)
    freq = np.fft.fftfreq(N,1/fd)
    mask = (np.abs(freq) < con.F0) | (np.abs(freq) > con.Fn)
    spectr[mask] = 0

    noise = np.fft.ifft(spectr).real

    noise_power = np.mean(noise**2)

     
    signal_power = np.mean(data**2)
    noise = noise* np.sqrt(signal_power/noise_power)

    data += noise
    data = data/np.max(np.abs(data))

    fig,axes = plt.subplots(2,1,figsize= (12,8))

    t = np.linspace(con.TMIN, con.TMAX, N)

    final_freqs = np.fft.fftfreq(N,d = 1/fd)
    final_spectr = np.abs(np.fft.fft(data)) / N

    axes[0].plot(t,data)
    axes[0].set_title("S(t)")
    axes[0].set_xlabel("t, s")
    axes[0].set_ylabel("A")
    axes[0].grid(True)

    axes[1].plot(final_freqs[:N//2],final_spectr[:N//2])
    axes[1].set_title("S(f)")
    axes[1].set_xlabel("f, Hz")
    axes[1].set_ylabel("A")
    axes[1].grid(True)

    gen.generateSignalintoFile(data,fd, con.NOISE)
    plt.tight_layout()
    plt.show()

def SubTask4():
    fd, data = gen.readFromFile(con.NOISE)
    data = data/np.max(np.abs(data)) 
    N = len(data)
    window = np.ones(con.M0)/ con.M0
    rez = np.convolve(data,window,mode='same')
    rez = rez/np.max(np.abs(rez))

    t = np.linspace(con.TMIN,con.TMAX,N)

    spectr1 = np.abs(np.fft.fft(data)) / N
    spectr2 = np.abs(np.fft.fft(rez)) / N

    freq = np.fft.fftfreq(N, 1/fd)


    fig,axes = plt.subplots(2,2,figsize=(12,8))
    
    axes[0][0].plot(t,data)
    axes[0][0].set_title("S(t)")
    axes[0][0].set_xlabel("t, s")
    axes[0][0].set_ylabel("A")
    axes[0][0].grid(True)

    axes[0][1].plot(t, rez)
    axes[0][1].set_title("S_optimized")
    axes[0][1].set_xlabel("t, s")
    axes[0][1].set_ylabel("A")
    axes[0][1].grid(True)

    axes[1][0].plot(freq[:N//2], spectr1[:N//2])
    axes[1][0].set_title("S(f)")
    axes[1][0].set_xlabel("f, Hz")
    axes[1][0].set_ylabel("A")
    axes[1][0].grid(True)

    axes[1][1].plot(freq[:N//2], spectr2[:N//2])
    axes[1][1].set_title("S(f) optimized")
    axes[1][1].set_xlabel("f, Hz")
    axes[1][1].set_ylabel("A")
    axes[1][1].grid(True)
    
    gen.generateSignalintoFile(rez,fd, con.WINDOW)
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="номер задания")
    parser.add_argument("--mode", 
                        choices=["generate","TF", "noise","window"],
                        required=True,
                        help="generate-сгенерировать, TF - временная и частотная область изначального сигнала, noise - добавление шума")
    args = parser.parse_args()
    if args.mode == "generate":
        SubTask1()
    elif args.mode == "TF":
        SubTask2()
    elif args.mode == "noise":
        SubTask3()
    elif args.mode == "window":
        SubTask4()
        

if __name__ == "__main__":
    main()  