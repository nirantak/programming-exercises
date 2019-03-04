"""
Backpropagation Algorithm
This Program runs with following constraints:
    1) It comprises of only 'One Hidden Layer' between Input and Output Layer.
    2) Every Layer consists of only 'Two Nodes'.
"""

import math

Input = [float(x) for x in input("\nEnter Two Inputs [i1, i2]: ").split()]
Bias = [float(x) for x in input("Enter Two Bias [b1, b2]: ").split()]
Weights = [
    float(x) for x in input("Enter Eight Weights [w1, w2, w3, w4, w5, w6, w7, w8]: ").split()
]
Output = [float(x) for x in input("Enter Two Target Outputs [o1, o2]: ").split()]
L_Val = float(input("Enter Lambda Value: "))
L_Rate = float(input("Enter Learning Rate: "))


print(
    f"""Inputs: {Input}
    Weights: {Weights}
    Bias: {Bias}
    Lambda Value: {L_Val}
    Learning Rate: {L_Rate}
    Target Output: {Output}
    """
)


def forward_pass(i, w, b, c):
    net = i[0] * w[0] + i[1] * w[1] + b * c
    out = 1 / (1 + math.exp(-c * net))
    return [net, out]


def Obackward_pass(OO, TO, H, W, c):
    NW = []
    value1 = (OO[0] - TO[0]) * OO[0] * (1 - OO[0]) * H[0]
    value2 = (OO[1] - TO[1]) * OO[1] * (1 - OO[1]) * H[1]
    for x in range(0, len(W)):
        if x < 2:
            W[x] = W[x] - c * value1
        else:
            W[x] = W[x] - c * value2
        NW.append(W[x])
    return NW


def Hbackward_pass(OO, TO, H, I, W, c):
    NW = []
    value1 = (
        (
            (OO[0] - TO[0]) * OO[0] * (1 - OO[0]) * W[4]
            + (OO[1] - TO[1]) * OO[1] * (1 - OO[1]) * W[6]
        )
        * H[0]
        * (1 - H[0])
        * I[0]
    )
    value2 = (
        (
            (OO[0] - TO[0]) * OO[0] * (1 - OO[0]) * W[5]
            + (OO[1] - TO[1]) * OO[1] * (1 - OO[1]) * W[7]
        )
        * H[1]
        * (1 - H[1])
        * I[1]
    )
    for x in range(0, len(W[0:4])):
        if x % 2 == 0:
            W[x] = W[x] - c * value1
        else:
            W[x] = W[x] - c * value2
        NW.append(W[x])
    return NW


Count = 0

while Count <= 10000:
    Count += 1
    H1 = forward_pass(Input, Weights[0:2], Bias[0], L_Val)
    H2 = forward_pass(Input, Weights[2:4], Bias[0], L_Val)
    O1 = forward_pass([H1[1], H2[1]], Weights[4:6], Bias[1], L_Val)
    O2 = forward_pass([H1[1], H2[1]], Weights[6:], Bias[1], L_Val)
    ErrorO1 = 0.5 * (Output[0] - O1[1]) * (Output[0] - O1[1])
    ErrorO2 = 0.5 * (Output[1] - O2[1]) * (Output[1] - O2[1])
    ErrorT = ErrorO1 + ErrorO2
    if Count == 1:
        print("\nForward Pass\n---------------")
        print(f"\nCount: {Count}")
        print(
            f"""
        NetH1: {H1[0]}
            OH1: {H1[1]}
            NetH2: {H2[0]}
            OH2: {H2[1]}
            """
        )
        print(
            f"""
        NetO1: {O1[0]}
            OO1: {O1[1]}
            NetO2: {O2[0]}
            OO2: {O2[1]}
            """
        )
        print(
            f"""
        ErrorO1: {ErrorO1}
            ErrorO2: {ErrorO2}
            Total Error: {ErrorT}
            """
        )

    if ErrorT != 0.000:
        W1 = Obackward_pass([O1[1], O2[1]], Output, [H1[1], H2[1]], Weights[4:], L_Rate)
        W2 = Hbackward_pass([O1[1], O2[1]], Output, [H1[1], H2[1]], Input, Weights, L_Rate)
        Weights = []
        Weights = W2 + W1
        if Count == 1:
            print("\nBackward Pass\n---------------")
            print(f"\nUpdated Weights: {Weights}")

print("\nForward Pass\n---------------")
print(f"\nCount: {Count}")
print(
    f"""
NetH1: {H1[0]}
    OH1: {H1[1]}
    NetH2: {H2[0]}
    OH2: {H2[1]}
    """
)
print(
    f"""
NetO1: {O1[0]}
    OO1: {O1[1]}
    NetO2: {O2[0]}
    OO2: {O2[1]}
    """
)
print(
    f"""
ErrorO1: {ErrorO1}
    ErrorO2: {ErrorO2}
    Total Error: {ErrorT}
    """
)

print("\nBackward Pass\n---------------")
print(f"\nUpdated Weights: {Weights}")
