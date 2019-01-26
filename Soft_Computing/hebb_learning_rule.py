"""
Implementation of Hebb Learning Rule.
Delta W = C * Oi * Xi
New Weight = Old Weight + Delta W
"""
from textwrap import dedent

import numpy as np

from .utils import activate_bipolar_sigmoid, activate_bipolar_step


def main(x: np.array, weight: np.array, fn: int):
    const = 1
    print(f"\nWeight 1: {weight}")

    for i, xi in enumerate(x):
        net = np.matmul(weight, xi)
        print(f"Net {i+1}: {net}")

        if fn == 1:
            out = activate_bipolar_step(net)
        elif fn == 2:
            out = activate_bipolar_sigmoid(net)
        else:
            return None

        print(f"Out {i+1}: {out}")

        deltaw = const * out * xi
        print(f"Delta W: {deltaw}")

        weight += deltaw
        print(f"\nWeight {i + 2}: {weight}")

    return weight


if __name__ == "__main__":
    n = int(input("Enter number of 1D input vectors: "))

    if n > 1:
        x = np.array(
            [float(j) for j in input(f"Enter elements in x1: ").split()], dtype=np.float
        )  # input vector
        ln = len(x)

        for i in range(n - 1):
            xi = np.array(
                [float(j) for j in input(f"Enter elements in x{i+2}: ").split()], dtype=np.float
            )
            x = np.vstack((x, xi))

        w = np.array([float(j) for j in input(f"Enter initial weights: ").split()], dtype=np.float)
        if len(w) != ln:
            print("... Using default weights")
            w = np.zeros(ln)

        fn = int(
            input(
                dedent(
                    """
                    1> Bipolar Step
                    2> Bipolar Sigmoidal
                    Choose activation function: """
                )
            )
        )

        w = main(x, w, fn)
        print(f"\nFinal weights are: {w}")
