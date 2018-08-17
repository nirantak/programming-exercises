"""
Spiral Primes, refer spiral_primes.md for the question.
"""

from itertools import cycle
from typing import Tuple


def gen_primes() -> int:
    """Infinite Prime Number Generator"""
    primes = set()
    n = 1
    while True:
        n += 1
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n


def gen_spiral() -> Tuple[int, Tuple[int, int]]:
    """Infinite Spiral Co-ordinates generator"""
    moves = [right, up, left, down]
    _moves = cycle(moves)
    prime = gen_primes()
    coordinates = 0, 0
    t = 1

    yield next(prime), coordinates

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(t):
                coordinates = move(*coordinates)
                yield next(prime), coordinates
        t += 1


def right(x: int, y: int) -> Tuple[int, int]:
    """Move one step to the right"""
    return x + 1, y


def left(x: int, y: int) -> Tuple[int, int]:
    """Move one step to the left"""
    return x - 1, y


def up(x: int, y: int) -> Tuple[int, int]:
    """Move one step up"""
    return x, y + 1


def down(x: int, y: int) -> Tuple[int, int]:
    """Move one step down"""
    return x, y - 1


def main(data: str):
    n = int(data)
    coordinates = []
    for i in range(n):
        location = input()
        x, y = [int(i.strip()) for i in location.split(",")]
        coordinates.append((x, y))

    spiral = gen_spiral()

    while n > 0:
        prime, location = next(spiral)
        if location in coordinates:
            print(prime)
            n -= 1
            coordinates.remove(location)


if __name__ == "__main__":
    data = input()
    main(data)
