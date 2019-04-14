"""
Street Lights, refer street_lights.md for the question.
"""

from itertools import combinations
from typing import Dict, List, Tuple


def main(data: List[List[Tuple[int, int]]]) -> List[float]:
    result: List[float] = []

    for d in data:
        total_area: float = 0.0
        int_area: float = 0.0
        lights: List[Dict[str, int]] = []

        for i in d:
            p, h = i
            area = h ** 2
            lights.append(
                {"x1": p - h, "y1": 0, "x2": p + h, "y2": 0, "x3": p, "y3": h}
            )
            total_area += area

        for l in combinations(lights, 2):
            int_area += (
                max(
                    0, min(l[0]["x2"], l[1]["x2"]) - max(l[0]["x1"], l[1]["x1"])
                )
                / 2
            ) ** 2

        result.append(float(total_area - int_area))
    return result


if __name__ == "__main__":
    t: int = int(input("Enter number of tests: "))
    data: List[List[Tuple[int, int]]] = []

    for i in range(t):
        n = int(input(f"\nEnter number of lights (Test {i+1}): "))
        lights: List[Tuple[int, int]] = []

        for j in range(n):
            p, h = map(
                int, input(f"Enter position & height of light {j+1}: ").split()
            )
            lights.append((p, h))
        data.append(lights)

    result = main(data)
    print("*** Area Covered by Street Lights ***")
    print("\n".join([f"Test {i}: {area}" for i, area in enumerate(result, 1)]))
