class GaussianNumber:
    def __init__(self, real = 0, imaginary = 0):
        self.re = round(real)
        self.im = round(imaginary)

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __add__(self, other):
        return GaussianNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return GaussianNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return GaussianNumber(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re
        )

    def __truediv__(self, other):
        assert abs(other) != 0, f"(GaussianNumber) Division by zero {other}"

        divisor = other.re ** 2 + other.im ** 2
        return GaussianNumber(
            (self.re * other.re + self.im * other.im) / divisor,
            (self.im * other.re - self.re * other.im) / divisor
        )

    def __abs__(self) -> int: # norm function
        return self.re ** 2 + self.im ** 2

    @staticmethod
    def div_rem(a, b):
        quotient = a / b
        remainder = a - quotient * b
        return quotient, remainder

    @staticmethod
    def gcd(a, b):
        if abs(a) < abs(b):
            a, b = b, a

        while abs(b) > 0:
            a, b = b, GaussianNumber.div_rem(a, b)[1]

        return a

    @staticmethod
    def lcm(a, b):
        return GaussianNumber.div_rem(a * b, GaussianNumber.gcd(a, b))[0]
