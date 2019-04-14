"""
Learning rules for Artificial Neural Networks
Delta W = function()
New Weight = Old Weight + Delta W
"""
import numpy as np


def hebb(Oi: float, Xi: np.array, C: float = 1.0) -> np.array:
    """
    Hebb Learning Rule (Unsupervised)
    Delta W = C * Oi * Xi
    """
    return C * Oi * Xi


def perceptron(Di: float, Oi: float, Xi: np.array, C: float = 1.0) -> np.array:
    """
    Perceptron Learning Rule (Supervised)
    Delta W = C * (Di - Oi) * Xi
    """
    return C * (Di - Oi) * Xi


def delta(Di: float, Oi: float, Xi: np.array, C: float = 1.0) -> np.array:
    """
    Delta Learning Rule (Supervised)
    Delta W = C * (Di - Oi) * f' * Xi
    f' = 0.5 * (1 - Oi**2)
    """
    f_ = 0.5 * (1 - (Oi ** 2))
    return C * (Di - Oi) * f_ * Xi


def widrow_hoff(
    Di: float, Wi: np.array, Xi: np.array, C: float = 1.0
) -> np.array:
    """
    Widrow-Hoff Learning Rule (Least Mean Square) (Supervised)
    Delta W = C * r * Xi
    r = Di - Wi * Xi
    """
    r = Di - np.matmul(Wi, Xi)
    return C * r * Xi


def correlation(Di: float, Xi: np.array, C: float = 1.0) -> np.array:
    """
    Correlation Learning Rule (Supervised)
    Delta W = C * Di * Xi
    """
    return C * Di * Xi


def winner_take_all(Wm: np.array, Xi: np.array, C: float = 1.0) -> np.array:
    """
    Winner-Take-All Learning Rule (Unsupervised)
    Delta W = C * (Xi - Wm)
    """
    return C * (Xi - Wm)


def outstar(Di: np.array, Wi: np.array, beta: float = 1.0) -> np.array:
    """
    Outstar Learning Rule (Supervised)
    Delta W = beta * (Di - Wi)
    """
    return beta * (Di - Wi)
