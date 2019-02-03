"""
Implementation of Hebb Learning Rule to generate weights for pattern recognition.
Delta W = C * Oi * Xi
New Weight = Old Weight + Delta W
"""
import numpy as np


def main(X1: np.array, X2: np.array, Bi: np.array, OP: np.array) -> np.array:
    X1 = np.append(X1, Bi[0])
    X2 = np.append(X2, Bi[1])
    Xi = np.vstack((X1, X2))
    const = 1

    weights = np.zeros(len(Xi[0]))
    print(f"Initial weights: {weights}")

    for i, x in enumerate(Xi):
        for j, value in enumerate(x):
            weights[j] += const * value * OP[i]
        print(f"Updated weights: {weights}")

    return weights


if __name__ == "__main__":
    # Set input pattern as bipolar pixel values in a 3x3 grid
    X1 = np.array([1, 1, 1, -1, 1, -1, 1, 1, 1])  # Character 'I'
    X2 = np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])  # Character 'O'

    Bi = np.array([1, 1])  # Bias input for pattern X1, X2
    OP = np.array([1, -1])  # Desired output for pattern X1, X2

    w = main(X1, X2, Bi, OP)
    print(f"\nFinal weights are: {w}")
