"""
Implementation of Hebb Learning Rule for AND, OR operations.
Delta W = C * Oi * Xi
New Weight = Old Weight + Delta W
"""
import sys
from typing import Tuple

import numpy as np


def main(x1: np.array, x2: np.array, bi: np.array, op: np.array) -> Tuple[int, int, int]:
    const = 1
    w1 = w2 = bw = 0
    print(f"Initial weights:\n\tw1 = {w1}, w2 = {w2}, bw = {bw}")

    for i, xi in enumerate(zip(x1, x2, bi, op)):
        print(f"\nInput {i+1}: {xi[:-1]}, Output: {xi[3]}")

        w1 += const * xi[3] * xi[0]
        w2 += const * xi[3] * xi[1]
        bw += const * xi[3] * xi[2]
        print(f"Updated weights:\n\tw1 = {w1}, w2 = {w2}, bw = {bw}")

    return (w1, w2, bw)


if __name__ == "__main__":
    x1 = np.array([1, 1, -1, -1])
    x2 = np.array([1, -1, 1, -1])
    bi = np.array([1, 1, 1, 1])

    if len(sys.argv) < 2 or sys.argv[1] not in {"and", "or"}:
        print("\nUsage: hebb_learning_op.py {and|or}")
        sys.exit(1)

    if sys.argv[1] == "and":
        op = np.array([1, -1, -1, -1])
    elif sys.argv[1] == "or":
        op = np.array([1, 1, 1, -1])

    w = main(x1, x2, bi, op)
    print(f"\nFinal weights are: {w}")
