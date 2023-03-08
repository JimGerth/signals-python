import matplotlib.pyplot as plt

from signals import Signals

if __name__ == '__main__':
    seed = 135
    length = 300
    shift = 82
    xlim = (shift, length)

    noise = Signals.noise(length, seed=seed)
    shifted = noise.shift(shift)
    correlated = noise.correlate(shifted)

    plt.figure(figsize=(6.5,4.5))
    plt.tight_layout()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    noise.plot(xlim=xlim, clear=True, show=True)

    plt.figure(figsize=(6.5,4.5))
    plt.tight_layout()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    shifted.plot(xlim=xlim, clear=True, show=True)

    plt.figure(figsize=(6.5,4.5))
    plt.tight_layout()
    plt.xlabel('Time delay')
    plt.ylabel('Correlation')
    correlated.plot(clear=True, show=True)
