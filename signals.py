from math import sin, cos, pi
import random

from signal import Signal

class Signals:
    @staticmethod
    def noise(length, *, gain=1, offset=0, seed=None):
        if seed is not None:
            random.seed(seed)
        return Signal(
            [random.gauss(0, gain) for i in range(offset + length)],
            offset=offset
        )

    @staticmethod
    def rect(length, *, gain=1, offset=0):
        return Signal(
            [gain for _ in range(length)],
            offset=offset,
        )

    @staticmethod
    def sin(length, *, f, fs, phase, offset=0):
        pass

    @staticmethod
    def cos(length, *, f, fs, phase, offset=0):
        pass
