"""
Implement Fuzzy set operations like - Union, Intersection, Complement, Difference, DeMorgan's Law
"""
import json
from textwrap import dedent
from typing import Dict, Tuple

from .fuzzy_sets import complement, difference, intersection, union


def demorgan(
    set1: Dict[str, int], set2: Dict[str, int]
) -> Tuple[bool, Dict[str, int], Dict[str, int]]:
    lhs = complement(union(set1, set2))
    rhs = intersection(complement(set1), complement(set2))

    out = json.dumps(lhs, sort_keys=True) == json.dumps(rhs, sort_keys=True)

    return (out, lhs, rhs)


def get_output(x: Dict[str, int]) -> str:
    return f"{{{', '.join(sorted((f'({key}, {value})' for key, value in x.items())))}}}"


def main(choice: int, set1: Dict[str, int], set2: Dict[str, int] = None):
    if choice == 1:
        result = union(set1, set2)
    elif choice == 2:
        result = intersection(set1, set2)
    elif choice == 3:
        result = complement(set1)
    elif choice == 4:
        result = difference(set1, set2)
    elif choice == 5:
        result = demorgan(set1, set2)
    else:
        return f"Invalid choice {choice}!!!"

    return result


if __name__ == "__main__":
    choices = ["Union", "Intersection", "Complement", "Difference", "Proof of DeMorgan's Law"]
    choice = int(
        input(
            dedent(
                """
    1. Union
    2. Intersection
    3. Complement
    4. Difference set1/set2
    5. Prove DeMorgan's Law
    Enter operation: """
            )
        )
    )

    set1 = {}
    for i in input("\nEnter set1 (k1 v1, k2 v2...): ").split(","):
        key, value = i.split()
        set1[key] = float(value)

    if choice != 3:
        set2 = {}
        for i in input("Enter set2 (k1 v1, k2 v2...): ").split(","):
            key, value = i.split()
            set2[key] = float(value)

        result = main(choice, set1, set2)
    else:
        result = main(choice, set1)

    print(f"\nResult: {choices[choice-1]}")
    if choice == 5:
        print(f"\t{result[0]}")
        print(f"\tLHS: {get_output(result[1])}")
        print(f"\tRHS: {get_output(result[2])}")
    else:
        print(f"\t{get_output(result)}")
