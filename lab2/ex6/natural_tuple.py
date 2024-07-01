from typing import Iterable


class NaturalTuple:
    def __init__(self, elements: Iterable[int]):
        if not all(e >= 0 for e in elements):
            raise ValueError("Cannot initialize a NaturalTuple object with negative values")

        self._tuple = tuple(elements)

    def __len__(self) -> int:
        return len(self._tuple)

    def __getitem__(self, index) -> int:
        return self._tuple[index]

    def __str__(self) -> str:
        return str(self._tuple)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, NaturalTuple):
            raise TypeError("Cannot compare NaturalTuple to a non NaturalTuple object")

        if len(self) != len(other):
            raise ValueError("Cannot compare tuples of different lengths")

        return all(lhs == rhs for (lhs, rhs) in zip(self._tuple, other._tuple))

    def __le__(self, other) -> bool:
        if not isinstance(other, NaturalTuple):
            raise TypeError("Cannot compare NaturalTuple to a non NaturalTuple object")

        if len(self) != len(other):
            raise ValueError("Cannot compare tuples of different lengths")

        return all(lhs <= rhs for (lhs, rhs) in zip(self._tuple, other._tuple))


def minimal_elements(A: Iterable[NaturalTuple]) -> list[NaturalTuple]:
    M = []
    for x in A:
        M = [m for m in M if not x <= m]  # Remove elements from M that are <= x
        if not any(m <= x for m in M):    # Check if x is not less than any element in M
            M.append(x)

    return M
