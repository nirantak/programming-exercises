"""
Spiral Primes, refer spiral_primes.md for the question.
"""

from itertools import cycle
from typing import List, Tuple


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


def main(n: int, coordinates: List[Tuple]) -> List[int]:
    result = []
    if len(coordinates) != n:
        print("Invalid Input")
        return None

    spiral = gen_spiral()

    while n > 0:
        prime, location = next(spiral)
        if location in coordinates:
            result.append(prime)
            n -= 1
            coordinates.remove(location)

    return result


if __name__ == "__main__":
    n = int(input("Enter number of co-ordinates: "))
    data = input("Enter list of coordinates separated by a comma: ")

    coordinates = []
    for i in data.split(","):
        x, y = i.split()
        coordinates.append((int(x), int(y)))

    result = main(n, coordinates)
    print(f"Primes: {result}")
