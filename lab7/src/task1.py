import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
import argparse

parent = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0,parent)

import lab1.scripts.generate as gen
import lab7.config as con

def SubTask1():
    t, data = con.Signal()

    data = data / np.max(np.abs(data))
    N = len(data)

    freqs = np.fft.fftfreq(N,1/con.FD)[:N//2]
    spectr = (np.abs(np.fft.fft(data)) / N)[:N//2]

    figure, axes = plt.subplots(1,2, figsize=(12,8))
    axes[0].plot(t,data)
    # axes[0].set_xlim(0,0.007)
    axes[1].plot(freqs,spectr)

    plt.tight_layout()
    plt.show()
    
def SubTask2():
    t, x = con.Signal()
    ns = int(con.FD * con.Tsym)                 

    i_sig =  x * np.cos(2*np.pi*con.Fc*t) 
    q_sig = -x * np.sin(2*np.pi*con.Fc*t) 

    bits = []
    for k in range(len(x) // ns):               
        sl = slice(k*ns, (k+1)*ns)               
        I = np.sum(i_sig[sl])                   
        Q = np.sum(q_sig[sl])
        phi = np.arctan2(Q, I) % (2*np.pi)      

        best = min(con.PHASE,
                   key=lambda b: abs(np.angle(np.exp(1j*(phi - con.PHASE[b])))))
        bits.extend(best)                       
    print(bits)
    print(bits == con.A)                        





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