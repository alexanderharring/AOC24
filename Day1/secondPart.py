from collections import Counter

c = Counter()
l1 = []
with open("input.txt") as files:

    for line in files:

        x = line.strip().split()

        l1.append(int(x[0]))
        
        c[int(x[1])] += 1

s = 0

for m in l1:
    s += m * c[m]

print(s)