class Signal(list):
    def __init__(self, signal, offset=0):
        super().__init__(signal)
        self.offset = offset

    def __getitem__(self, index):
        index -= self.offset
        if index >= 0 and index < len(self):
            return list(self)[index]
        else:
            return 0

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return Signal(
                [self[i] + other for i in range(self.offset, self.offset + len(self))],
                offset=self.offset
            )

        elif type(other) is Signal:
            offset = min(self.offset, other.offset)
            length = max(self.offset + len(self), other.offset + len(other))
            return Signal(
                [self[i] + other[i] for i in range(offset, length)],
                offset=offset
            )

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return Signal(
                [self[i] - other for i in range(self.offset, self.offset + len(self))],
                offset=self.offset
            )

        elif type(other) is Signal:
            offset = min(self.offset, other.offset)
            length = max(self.offset + len(self), other.offset + len(other))
            return Signal(
                [self[i] - other[i] for i in range(offset, length)],
                offset=offset
            )

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Signal(
                [self[i] * other for i in range(self.offset, self.offset + len(self))],
                offset=self.offset
            )

        elif type(other) is Signal:
            offset = min(self.offset, other.offset)
            length = max(self.offset + len(self), other.offset + len(other))
            return Signal(
                [self[i] * other[i] for i in range(offset, length)],
                offset=offset
            )

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return Signal(
                [self[i] / other for i in range(self.offset, self.offset + len(self))],
                offset=self.offset
            )

        elif type(other) is Signal:
            offset = min(self.offset, other.offset)
            length = max(self.offset + len(self), other.offset + len(other))
            return Signal(
                [self[i] / other[i] for i in range(offset, length)],
                offset=offset
            )

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return Signal(
                [self[i] // other for i in range(self.offset, self.offset + len(self))],
                offset=self.offset
            )

        elif type(other) is Signal:
            offset = min(self.offset, other.offset)
            length = max(self.offset + len(self), other.offset + len(other))
            return Signal(
                [self[i] // other[i] for i in range(offset, length)],
                offset=offset
            )

    def __str__(self):
        string = '['
        for i in self.range():
            if i == 0:
                string += f'({self[i]}), '
            else:
                string += f'{self[i]}, '
        string = string[:-2]
        string += ']'
        return string

    def __repr__(self):
        return str(self)

    def range(self):
        return range(self.offset, self.offset + len(self))

    def shift(self, lag):
        return Signal(list(self), offset=self.offset + lag)

    def correlate(self, other):
        assert(type(other) is Signal)
        min_shift = self.offset - (other.offset + len(other) - 1)
        max_shift = (self.offset + len(self)) - other.offset
        return Signal(
            [sum(self * other.shift(lag)) for lag in range(min_shift, max_shift)],
            offset=min_shift
        )

    def plot(self, *, xlim=None, clear=False, show=False):
        import matplotlib.pyplot as plt

        if clear:
            plt.clf()

        x = list(self.range())
        plt.plot(x, self)
        ticks = plt.xticks()[0]
        plt.xticks(ticks[ticks % 1 == 0])
        plt.xlim(xlim if xlim is not None else (min(x), max(x)))

        if show:
            plt.show()
