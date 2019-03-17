"""
Fuzzy Set Operations
"""
from typing import Dict, List


def union(set1: Dict[str, int], set2: Dict[str, int]) -> Dict[str, int]:
    elements1 = {key for key, value in set1.items()}
    elements2 = {key for key, value in set2.items()}
    elements = elements1.union(elements2)
    result = {}

    for e in elements:
        result[e] = max(set1.get(e, 0), set2.get(e, 0))
        if result[e] == 0:
            result.pop(e)

    return result


def intersection(set1: Dict[str, int], set2: Dict[str, int]) -> Dict[str, int]:
    elements1 = {key for key, value in set1.items()}
    elements2 = {key for key, value in set2.items()}
    elements = elements1.union(elements2)
    result = {}

    for e in elements:
        result[e] = min(set1.get(e, 0), set2.get(e, 0))
        if result[e] == 0:
            result.pop(e)

    return result


def complement(set1: Dict[str, int]) -> Dict[str, int]:
    result = {}

    for e in set1:
        result[e] = round(1 - set1.get(e, 0), 2)
        if result[e] == 0:
            result.pop(e)

    return result


def difference(set1: Dict[str, int], set2: Dict[str, int]) -> Dict[str, int]:
    return intersection(set1, complement(set2))


def max_min(a: List[List[float]], b: List[List[float]]):
    zip_b = list(zip(*b))
    return [
        [max(min(ele_a, ele_b) for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b]
        for row_a in a
    ]


def max_product(a: List[List[float]], b: List[List[float]]):
    zip_b = list(zip(*b))
    return [
        [round(max(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)), 3) for col_b in zip_b]
        for row_a in a
    ]
