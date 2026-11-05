import math
import matplotlib.pyplot as plt

"""
C = capacidade do canal (bps);
B = largura de banda (Hz);
N = número de níveis de sinalização;
SNR = razão sinal-ruído em escala linear.
"""

# Implemente os modelos

def nyquist(b, n):
    capacity = 2 * b * math.log2(n)
    return capacity

def shannon(b, snr):
    capacity = b * math.log2(1 + (snr))
    return capacity

# Experimento 1 – Capacidade de Nyquist
def exp_um():
    ns = [2, 4, 8, 16]
    bandas = [1.5, 10]

    for b in bandas:
        capacidades = [nyquist(b, n) for n in ns]
        plt.plot(ns, capacidades, marker="o", label=f"B = {b}")

    plt.xlabel("Número de níveis de sinalização (N)")
    plt.ylabel("Capacidade do canal (C)")
    plt.title("Capacidade de Nyquist: C versus N")
    plt.xticks(ns)
    plt.grid(True)
    plt.legend()
    plt.show()

# Experimento 2 – Capacidade de Shannon
def exp_dois():
    snrs = [1000, 5000, 10000, 50000]
    bandas = range(0, 11)

    for snr in snrs:
        capacidades = [shannon(b, snr) for b in bandas]
        plt.plot(bandas, capacidades, marker="o", label=f"SNR = {snr}")

    plt.xlabel("Largura de banda (B)")
    plt.ylabel("Capacidade do canal (C)")
    plt.title("Capacidade de Shannon: C versus B")
    plt.grid(True)
    plt.legend()
    plt.show()

def exp_tres():
    b = 5
    snrs = 41 #dB
    capacidades = []

    for snr in range (1, snrs, 5):
        snr_linear = 10 ** (snr / 10)  # Convertendo dB para escala linear
        capacidades.append(shannon(b, snr_linear))

    plt.plot(range(1, snrs, 5), capacidades, marker="o", label=f"B = {b} Hz")

    plt.xlabel("SNR (dB)")
    plt.ylabel("Capacidade do canal (C)")
    plt.title("Capacidade de Shannon: C versus SNR")
    plt.grid(True)
    plt.legend()
    plt.show()

def exp_quatro():
    b = 3
    snr = 30 #dB
    n = [2, 4, 8, 16, 32, 64]

    snr_linear = 10 ** (snr / 10)
    capacidades_nyquist = [nyquist(b, niveis) for niveis in n]
    capacidade_shannon = shannon(b, snr_linear)

    plt.plot(n, capacidades_nyquist, marker="o", label="Nyquist")
    plt.axhline(capacidade_shannon, linestyle="--", label="Limite de Shannon")

    plt.xlabel("Número de níveis de sinalização (N)")
    plt.ylabel("Capacidade do canal (bps)")
    plt.title(f"Capacidade de Nyquist e limite de Shannon (B = {b} Hz, SNR = {snr} dB)")
    plt.xticks(n)
    plt.grid(True)
    plt.legend()
    plt.show()

exp_quatro()
    