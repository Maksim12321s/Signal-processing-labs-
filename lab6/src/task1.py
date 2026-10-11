import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
import argparse

parent = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0,parent)

import lab1.scripts.generate as gen
import lab6.config as con

def SubTask1():
    N = int(con.DUR*con.FD)
    t = np.linspace(0,con.DUR,N)
    s = con.Signal(t)

    freqs = np.fft.fftfreq(N,1.0/con.FD)
    freqs = freqs[:N//2]
    spec = np.abs(np.fft.fft(s)) /N
    spec = spec[:N//2]
    fig, axes = plt.subplots(1,2,figsize=(12,8))
    
    axes[0].plot(t,s)
    axes[1].plot(freqs, spec)
    axes[0].set_xlim(0, 0.01)

    plt.tight_layout()
    plt.show()
    gen.generateSignalintoFile(s,con.FD,con.ORIG)
def SubTask2():
    fd,data = gen.readFromFile(con.ORIG)
    N = len(data)
    data = data/np.max(np.abs(data))
    
    t = np.linspace(0,con.DUR,N)
    data1 = con.Signal(t)

    newdata = data*data1

   
    Fcp = con.FNEW // 2
    h = con.highpass(Fcp,fd,100)
    filtered = np.convolve(newdata,h,mode="same")

    def spec(s):
        return (np.abs(np.fft.fft(s)) / N)[:N//2]

    freqs = np.fft.fftfreq(N,1/fd)
    freqs = freqs[:N//2]

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    for ax, s, title in zip(axes,
                            [data, newdata, filtered],
                            ["Исходный", "После гетеродинирования", "После ФВЧ"]):
        ax.plot(freqs, spec(s))
        ax.set_title(title)
        ax.set_xlabel("f, Hz")
        ax.set_ylabel("A")
        ax.grid(True)
    plt.tight_layout()
    plt.show()
    gen.generateSignalintoFile(filtered,fd,con.FILTER)







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


if __name__ == "__main__":
    main()