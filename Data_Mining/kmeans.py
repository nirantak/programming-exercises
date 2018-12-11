"""
Find clusters for input dataset using KMeans Algorithm.
"""
from typing import List


def main(data: List[int], m1: float, m2: float):
    print(f"\n\tDataset: {data}")
    print(f"\tMeans: m1={m1}, m2={m2} \n")

    while True:
        k1 = []
        k2 = []
        c1 = c2 = sum1 = sum2 = 0
        pm1, pm2 = m1, m2

        for i in data:
            if abs(m1 - i) < abs(m2 - i):
                k1.append(i)
                c1 += 1
            else:
                k2.append(i)
                c2 += 1

        print(f"\tk1: {k1}")
        print(f"\tk2: {k2}")

        for i in range(c1):
            sum1 += k1[i]
        m1 = sum1 / c1

        for i in range(c2):
            sum2 += k2[i]
        m2 = sum2 / c2

        print(f"\tThe new means for k1 and k2 are: m1={m1}, m2={m2} \n")
        if pm1 == m1 and pm2 == m2:
            break

    print("Since new mean is equal to mean obtained in the last step, execution is stopped here.")


if __name__ == "__main__":
    x = input("Enter the dataset: ")
    data = list(map(int, x.split()))

    x = input("Enter 2 mean values(m1 and m2): ")
    m1, m2 = map(float, x.split())
    main(data, m1, m2)
