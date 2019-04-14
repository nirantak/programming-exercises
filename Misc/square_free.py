"""
Square Free Numbers, refer square_free.md for the question.
"""

from math import sqrt
from typing import List


def factors(num: int) -> List[int]:
    """Find factors of a given input number"""
    result = set(
        x
        for y in (
            [i, num // i] for i in range(2, int(num ** 0.5) + 1) if num % i == 0
        )
        for x in y
    )
    return list(result)


def main(num: int) -> int:
    count = 0

    fact = factors(num)
    for f in fact:
        if sqrt(f).is_integer():
            pass
        elif len([i for i in factors(f) if sqrt(i).is_integer()]):
            pass
        else:
            count += 1

    return count


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = main(num)
    print(f"Number of square free factors: {result}")
