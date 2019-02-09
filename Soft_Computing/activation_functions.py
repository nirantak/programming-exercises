"""
Activation Functions for Artificial Neural Networks
"""

import math


def binary_step(n: float):
    """
    Binary Step (Unipolar Binary) Activation Function
    """
    if n >= 0:
        return 1
    return 0


def bipolar_step(n: float):
    """
    Bipolar Step (Bipolar Binary) Activation Function
    """
    if n >= 0:
        return 1
    return -1


def binary_sigmoid(n: float, lmbda: float = 1.0):
    """
    Binary Sigmoidal (Unipolar Continuous) Activation Function
    """
    return 1 / (1 + (math.exp(-lmbda * n)))


def bipolar_sigmoid(n: float, lmbda: float = 1.0):
    """
    Bipolar Sigmoidal (Bipolar Continuous) Activation Function
    """
    return (2 / (1 + (math.exp(-lmbda * n)))) - 1
