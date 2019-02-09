"""
Neural Network to implement XOR gate using McCulloch-Pitts Neuron Model.
"""
import numpy as np

from .neurons import neuron


def main():
    print("\n*** Neural Network for XOR Operation ***")
    print("\ny = z1 + z2 = x1.x2' + x1'.x2")

    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])

    z1: np.array = np.logical_and(x1, (1 - x2)).astype(int)
    z2: np.array = np.logical_and((1 - x1), x2).astype(int)

    y: np.array = np.logical_or(z1, z2).astype(int)

    ops = [
        {"op": "and", "x1": x1, "x2": x2, "out": z1},
        {"op": "and", "x1": x1, "x2": x2, "out": z2},
        {"op": "or", "x1": z1, "x2": z2, "out": y},
    ]

    i = 0
    while i < len(ops):
        w1 = int(input(f"\nEnter Value for Weight w{i}1: "))
        w2 = int(input(f"Enter Value for Weight w{i}2: "))

        res = neuron(ops[i]["x1"], ops[i]["x2"], ops[i]["out"], w1, w2)

        print(f"\n\tX1\tX2\tNet{i}\tO{i}")
        for j in res[2]:
            print(f"\t{j['x1']}\t{j['x2']}\t{j['net']}\t{j['output']}")

        if res[0]:
            print("\nYour Weights are Correct!")
            print(f"\nThreshold Value: {res[1]}")
            i += 1
        else:
            print("\nYour Weights are Incorrect! No Net Value satisfies Threshold Constraints.")
            print("\nEnter weights again...")


if __name__ == "__main__":
    main()
