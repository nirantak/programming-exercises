"""
Reusable utility functions
"""
from typing import Dict, List, Tuple

import numpy as np


def neuron(
    x1: np.array, x2: np.array, output: np.array, w1: int, w2: int
) -> Tuple[bool, int, Dict[str, int]]:
    """
    Model of an Artificial Neuron to check weights for a given set of inputs and desired outputs.
    """
    data: List[Dict[str, int]] = []

    net: np.array = x1 * w1 + x2 * w2
    anet = np.array([], dtype=int)

    for n, out in enumerate(output):
        if out == 1:
            anet = np.append(anet, net[n])

    anet.sort()

    count: int = 0
    for n in net:
        if n >= anet[0]:
            count += 1

    for i, out in enumerate(output):
        data.append({"x1": x1[i], "x2": x2[i], "net": net[i], "output": out})

    if len(anet) == count:
        return (True, anet[0], data)
    else:
        return (False, 0, data)
