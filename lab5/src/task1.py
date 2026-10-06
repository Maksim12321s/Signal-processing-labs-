import sys
from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

parent = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0,parent)

import lab1.scripts.generate as gen
import lab5.config as con



def SubTask1():
    N = con.DUR * con.FD
    t = np.linspace(0,con.DUR, N)
    s = con.Signal(t)

    spectr = np.abs(np.fft.fft(s)) / N
    freqs = np.fft.fftfreq(N, 1/con.FD)

    figure, axis = plt.subplots(1,2, figsize= (12,8))

    axis[0].plot(t,s)
    axis[0].grid(True)

    axis[1].plot(freqs[:N//2], spectr[:N//2])
    axis[1].grid(True)

    s = s / np.max(np.abs(s))
    gen.generateSignalintoFile(s,con.FD, con.ORIG)

    plt.tight_layout()
    plt.show()

def SubTask2():
    fd, data = gen.readFromFile(con.ORIG)
    if data.ndim > 1:
        data = data.mean(axis=1)
    data = data / np.max(np.abs(data))

    symbol, f_low, f_high, a_low, a_high = con.detect_dtmf(data, fd)
    print(f"Найденные частоты: {f_low} Гц и {f_high} Гц")
    print(f"Символ: {symbol}")

    plt.bar([str(f) for f in con.LOW + con.HIGH],a_low + a_high)
    plt.xlabel("f,Hz")
    plt.ylabel("A")
    plt.grid(True, axis='y')
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


if __name__ == "__main__":
    main()