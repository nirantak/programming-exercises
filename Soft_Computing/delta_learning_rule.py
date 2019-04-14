"""
Implementation of Delta Learning Rule.
Delta W = C * (Di - Oi) * f' * Xi
New Weight = Old Weight + Delta W
"""
import numpy as np

from .activation_functions import bipolar_sigmoid
from .learning_rules import delta


def main(x: np.array, weight: np.array, const: float, d: np.array) -> np.array:
    print(f"\nWeight 1: {weight}")

    for i, xi in enumerate(x):
        net = np.matmul(weight, xi)
        print(f"Net {i+1}: {net}")

        out = bipolar_sigmoid(net)
        print(f"Out {i+1}: {out}")

        weight += delta(d[i], out, xi, const)
        print(f"\nWeight {i + 2}: {weight}")

    return weight


if __name__ == "__main__":
    n = int(input("Enter number of 1D input vectors: "))
    const = float(input("Enter value of constant: "))

    if n > 1:
        x = np.array(
            [float(j) for j in input(f"Enter elements in x1: ").split()],
            dtype=np.float,
        )  # input vector
        ln = len(x)

        for i in range(n - 1):
            xi = np.array(
                [
                    float(j)
                    for j in input(f"Enter elements in x{i+2}: ").split()
                ],
                dtype=np.float,
            )
            x = np.vstack((x, xi))

        d = np.array(
            [
                float(j)
                for j in input(f"Enter values for desired output di: ").split()
            ],
            dtype=np.float,
        )  # di vector

        w = np.array(
            [float(j) for j in input(f"Enter initial weights: ").split()],
            dtype=np.float,
        )
        if len(w) != ln:
            print("... Using default weights")
            w = np.zeros(ln)

        w = main(x, w, const, d)
        print(f"\nFinal weights are: {w}")
