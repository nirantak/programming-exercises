"""
Neural Network to implement AND gate using McCulloch-Pitts Neuron Model.
"""
from typing import Dict, List, Tuple


def main(w1: int, w2: int) -> Tuple[bool, int, Dict[str, int]]:
    output: List[int] = []
    net: List[int] = []
    anet: List[int] = []
    data: List[Dict[str, int]] = []

    for x1 in range(0, 2):
        for x2 in range(0, 2):
            output.append(x1 and x2)

    for x1 in range(0, 2):
        for x2 in range(0, 2):
            net.append(w1 * x1 + w2 * x2)

    for n in range(0, 4):
        if output[n] == 1:
            anet.append(net[n])

    anet.sort()

    count: int = 0
    for n in range(0, 4):
        if net[n] >= anet[0]:
            count += 1

    i: int = 0
    for x1 in range(0, 2):
        for x2 in range(0, 2):
            data.append({"x1": x1, "x2": x2, "net": net[i], "output": output[i]})
            i += 1

    if len(anet) == count:
        return (True, anet[0], data)
    else:
        return (False, 0, data)


if __name__ == "__main__":
    print("\n*** Neural Network for AND Operation ***")
    w1 = int(input("\nEnter Value for Weight 1 (w1): "))
    w2 = int(input("Enter Value for Weight 2 (w2): "))

    res = main(w1, w2)
    print("\n\tX1\tX2\tNet\tO")
    for i in res[2]:
        print(f"\t{i['x1']}\t{i['x2']}\t{i['net']}\t{i['output']}")

    if res[0]:
        print("\nYour Weights are Correct!")
        print(f"\nThreshold Value: {res[1]}")
    else:
        print("\nYour Weights are Incorrect! No Net Value satisfies Threshold Constraints.")
