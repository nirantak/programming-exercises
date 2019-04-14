"""
Use Bayesian Classification to solve the given problem.
Dataset: bayes.csv
"""
from functools import reduce
from typing import Dict

import pandas as pd


def main(dataset_path: str, X: Dict):
    df = pd.read_csv(dataset_path, encoding="utf8")
    i = 0
    c_yes = 0
    c_no = 0

    pn_yes = []
    pn_no = []

    print("Dataset:")
    print(df)

    for index, row in df.iterrows():
        if row.buys_computer == "yes":
            c_yes += 1
        else:
            c_no += 1
    pc_yes = round(c_yes / 14, 3)
    pc_no = round(c_no / 14, 3)

    print("\nP(C\u1D62):")
    print(f"\tP(buys_computer = 'yes') = {pc_yes}")
    print(f"\tP(buys_computer = 'no') = {pc_no}")

    print(
        f"""
    X = (age {X['age']}, income = {X['income']},
    student = {X['student']}, credit_rating = {X['credit_rating']}
    """
    )

    print("\nP(X|C\u1D62) for each class:")
    for key, value in X.items():
        n_yes = 0
        n_no = 0
        for index, row in df.iterrows():
            if row.buys_computer == "yes" and row[key] == value:
                n_yes += 1
            elif row.buys_computer == "no" and row[key] == value:
                n_no += 1
        pn_yes.append(round(n_yes / 9, 3))
        pn_no.append(round(n_no / 5, 3))

        print(f"\tP({key} = {value}|buys_computer = 'yes') = {pn_yes[i]}")
        print(f"\tP({key} = {value}|buys_computer = 'no') = {pn_no[i]}")
        i += 1

    pxc_yes = round(reduce(lambda x, y: x * y, pn_yes, 1), 3)
    pxc_no = round(reduce(lambda x, y: x * y, pn_no, 1), 3)

    print("\nP(X|C\u1D62):")
    print(f"\tP(X|buys_computer = 'yes') = {pxc_yes}")
    print(f"\tP(X|buys_computer = 'no') = {pxc_no}")

    pcx_yes = pxc_yes * pc_yes
    pcx_no = pxc_no * pc_no
    print("\nP(C\u1D62|X) = P(X|C\u1D62)*P(C\u1D62):")
    print(
        f"\tP(X|buys_computer = 'yes') * P(buys_computer = 'yes') = {round(pcx_yes, 3)}"
    )
    print(
        f"\tP(X|buys_computer = 'no') * P(buys_computer = 'no') = {round(pcx_no, 3)}"
    )

    print(
        f"""
    The given query is classified as:
    'buys_computer' = '{'yes' if pcx_yes > pcx_no else 'no'}'
    """
    )


if __name__ == "__main__":
    X = {}
    X["age"] = input("\nEnter class for age: ")
    X["income"] = input("Enter class for income: ")
    X["student"] = input("Enter class for student: ")
    X["credit_rating"] = input("Enter class for credit_rating: ")
    main("bayes.csv", X)
