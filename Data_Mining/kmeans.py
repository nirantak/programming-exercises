"""
Find clusters for input dataset using KMeans Algorithm.
"""

x = input("Enter the dataset: ")
data = list(map(int, x.split()))

x = input("Enter 2 mean values(m1 and m2): ")
m1, m2 = map(float, x.split())

print("\n\tDataset: {}".format(data))
print("\tMeans: m1={}, m2={} \n".format(m1, m2))

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

    print("\tk1: {}".format(k1))
    print("\tk2: {}".format(k2))

    for i in range(c1):
        sum1 = sum1 + k1[i]
    m1 = sum1 / c1

    for i in range(c2):
        sum2 = sum2 + k2[i]
    m2 = sum2 / c2

    print("\tThe new means for k1 and k2 are: m1={}, m2={} \n".format(m1, m2))
    if pm1 == m1 and pm2 == m2:
        break

print(
    "Since new mean is equal to mean obtained in the last step,\
execution is stopped here."
)
