from math import sqrt


class ComplexNumber:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        if real < 0:
            self._real = real

    def __add__(self, other):
        return ComplexNumber(self._real + other._real, self._imag + other._imag)

    def __sub__(self, other):
        return ComplexNumber(self._real - other._real, self._imag - other._imag)

    def __len__(self):
        return int(sqrt(self._real**2 + self._imag**2))

    def __eq__(self, other):
        return self._real == other._real and self._imag == other._imag

    def __lt__(self, other):
        return len(self) < len(other)

    def __mul__(self, other):
        return ComplexNumber(
            self._real * other._real - self._imag * other._imag,
            self._real * other._imag + self._imag * other._real
        )


    def __repr__(self):
        return f"repr {self.__class__.__name__}({self._real}, {self._imag})"

    def __str__(self):
        return f"str {self.__class__.__name__}({self._real}, {self._imag})"



c1 = ComplexNumber(1, 4)
c2 = ComplexNumber(2, 3)

print(c1)
print([c1, c2])
c1.real



print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 == c2)
print(len(c1), len(c2))
print(c1 < c2)
