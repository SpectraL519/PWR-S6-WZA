from typing import Union

Numerical = Union[int, float]


def poly_deg(coefficients: list[Numerical]) -> int:
    return Polynomial(coefficients).degree()

def poly_lt(coefficients: list[Numerical]) -> Numerical:
    return Polynomial(coefficients).leading_term()


class Polynomial:
    def __init__(self, coefficients: list[Numerical]):
        self._coefficients = coefficients
        while len(self._coefficients) > 0 and self._coefficients[-1] == 0:
            del self._coefficients[-1]

    def degree(self) -> int:
        return len(self) - 1

    def leading_term(self) -> Numerical:
        return self._coefficients[-1]

    def __len__(self) -> int:
        return len(self._coefficients)

    def __getitem__(self, index) -> Numerical:
        return self._coefficients[index]

    def __str__(self) -> str:
        def _elem_str(c: Numerical, i: int) -> str:
            if i == 0:
                return f"{c}"

            if i == 1:
                return "x" if c == 1 else f"{c}x"

            return f"x^{i}" if c == 1 else f"{c}x^{i}"

        basic_str = " + ".join([_elem_str(c, i) for (i, c) in enumerate(self._coefficients)])
        return basic_str.replace(".0", "").replace("1x", "x")

    def __add__(self, other):
        return Polynomial.add(self, other)

    def __sub__(self, other):
        return Polynomial.sub(self, other)

    def __mul__(self, other):
        return Polynomial.mul(self, other)

    @staticmethod
    def add(f, g):
        fc, gc = f._coefficients, g._coefficients

        if len(f) > len(g):
            gc += [0] * (len(f) - len(g))
        elif len(f) < len(g):
            fc += [0] * (len(g) - len(f))

        return Polynomial(list(map(lambda x, y: x + y, fc, gc)))


    @staticmethod
    def sub(f, g):
        fc, gc = f._coefficients, g._coefficients

        if len(f) > len(g):
            gc += [0] * (len(f) - len(g))
        elif len(f) < len(g):
            fc += [0] * (len(g) - len(f))

        return Polynomial(list(map(lambda x, y: x - y, fc, gc)))


    @staticmethod
    def mul(f, g):
        h = [0] * (len(f) + len(g) - 1)
        for i in range(len(f)):
            for j in range(len(g)):
                h[i + j] += f[i] * g[j]
        return Polynomial(h)

    @staticmethod
    def div_rem(f, g):
        q = [0] * (len(f) - len(g) + 1)
        r = list(f._coefficients)

        gc = g._coefficients
        while poly_deg(r) >= poly_deg(gc):
            i = poly_deg(r) - poly_deg(gc)
            q[i] = poly_lt(r) / poly_lt(gc)
            for j in range(len(g)):
                r[i + j] -= q[i] * g[j]

        return Polynomial(q), Polynomial(r)

    @staticmethod
    def gcd(f, g):
        if f.degree() < g.degree():
            f, g = g, f

        while len(g) > 0:
            f, g = g, Polynomial.div_rem(f, g)[1]

        return f

    @staticmethod
    def lcm(f, g):
        return Polynomial.div_rem(f * g, Polynomial.gcd(f, g))[0]
