"""
Implement Fuzzy set relations like - Max-Min and Max-Product
"""
import sys
from textwrap import dedent
from typing import List

from .fuzzy_sets import max_min, max_product


def get_output(x: List[List[float]]) -> str:
    res = "\n ".join(str(i) for i in x)
    return f"[{res}]"


def main():
    choices = ["Max-Min", "Max-Product"]
    choice = int(
        input(
            dedent(
                """
                1. Max-Min
                2. Max-Product
                Enter operation: """
            )
        )
    )

    ma, na = [
        int(i) for i in input("Enter m n dimensions for relation1: ").split()
    ]
    mb, nb = [
        int(i) for i in input("Enter m n dimensions for relation2: ").split()
    ]

    a = []
    for i in input("\nEnter relation1 [[e11...e1n],[em1...emn]]: ").split(","):
        a.append([float(x) for x in i.split()])

    b = []
    for i in input("Enter relation2 [[e11...e1n],[em1...emn]]: ").split(","):
        b.append([float(x) for x in i.split()])

    if (
        (na != mb)
        or (ma != len(a))
        or (mb != len(b))
        or any(len(x) != na for x in a)
        or any(len(x) != nb for x in b)
    ):
        print("Invalid dimensions!")
        sys.exit(1)

    if choice == 1:
        result = max_min(a, b)
    elif choice == 2:
        result = max_product(a, b)
    else:
        print("Invalid choice!")
        sys.exit(1)

    print(f"\nResult: {choices[choice-1]}")
    print(f"{get_output(result)}")


if __name__ == "__main__":
    main()
