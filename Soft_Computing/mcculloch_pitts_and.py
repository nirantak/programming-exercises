"""
Neural Network to implement AND gate using McCulloch-Pitts Neuron Model.
"""
import numpy as np

from .utils import neuron


def main():
    print("\n*** Neural Network for AND Operation ***")
    print("\ny = x1 . x2")

    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])

    y: np.array = np.logical_and(x1, x2).astype(int)

    while True:
        w1 = int(input("\nEnter Value for Weight w1: "))
        w2 = int(input("Enter Value for Weight w2: "))

        res = neuron(x1, x2, y, w1, w2)
        print("\n\tX1\tX2\tNet\tO")
        for i in res[2]:
            print(f"\t{i['x1']}\t{i['x2']}\t{i['net']}\t{i['output']}")

        if res[0]:
            print("\nYour Weights are Correct!")
            print(f"\nThreshold Value: {res[1]}")
            break
        else:
            print("\nYour Weights are Incorrect! No Net Value satisfies Threshold Constraints.")
            print("\nEnter weights again...")


if __name__ == "__main__":
    main()
