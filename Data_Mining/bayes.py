"""
Use Bayesian Classification to solve the given problem.
Dataset: bayes.csv
"""
from functools import reduce

import pandas as pd

df = pd.read_csv("bayes.csv", encoding="utf8")
i = 0
c_yes = 0
c_no = 0
X = {}
pn_yes = []
pn_no = []

print("Dataset:")
print(df)

X["age"] = input("\nEnter class for age: ")
X["income"] = input("Enter class for income: ")
X["student"] = input("Enter class for student: ")
X["credit_rating"] = input("Enter class for credit_rating: ")

for index, row in df.iterrows():
    if row.buys_computer == "yes":
        c_yes = c_yes + 1
    else:
        c_no = c_no + 1
pc_yes = round(c_yes / 14, 3)
pc_no = round(c_no / 14, 3)

print(u"\nP(C\u1D62):")
print("\tP(buys_computer = 'yes') = {}".format(pc_yes))
print("\tP(buys_computer = 'no') = {}".format(pc_no))

print(
    "\nX = (age {}, income = {}, student = {}, credit_rating = {})".format(
        X["age"], X["income"], X["student"], X["credit_rating"]
    )
)

print(u"\nP(X|C\u1D62) for each class:")
for key, value in X.items():
    n_yes = 0
    n_no = 0
    for index, row in df.iterrows():
        if row.buys_computer == "yes" and row[key] == value:
            n_yes = n_yes + 1
        elif row.buys_computer == "no" and row[key] == value:
            n_no = n_no + 1
    pn_yes.append(round(n_yes / 9, 3))
    pn_no.append(round(n_no / 5, 3))

    print("\tP({} = {}|buys_computer = 'yes') = {}".format(key, value, pn_yes[i]))
    print("\tP({} = {}|buys_computer = 'no') = {}".format(key, value, pn_no[i]))
    i = i + 1

pxc_yes = round(reduce(lambda x, y: x * y, pn_yes, 1), 3)
pxc_no = round(reduce(lambda x, y: x * y, pn_no, 1), 3)

print(u"\nP(X|C\u1D62):")
print("\tP(X|buys_computer = 'yes') = {}".format(pxc_yes))
print("\tP(X|buys_computer = 'no') = {}".format(pxc_no))

pcx_yes = pxc_yes * pc_yes
pcx_no = pxc_no * pc_no
print(u"\nP(C\u1D62|X) = P(X|C\u1D62)*P(C\u1D62):")
print(
    "\tP(X|buys_computer = 'yes') * P(buys_computer = 'yes') = {}".format(
        round(pcx_yes, 3)
    )
)
print(
    "\tP(X|buys_computer = 'no') * P(buys_computer = 'no') = {}".format(
        round(pcx_no, 3)
    )
)

print(
    "\nThe given query is classified as: \n\t'buys_computer' = '{}'".format(
        "yes" if pcx_yes > pcx_no else "no"
    )
)
