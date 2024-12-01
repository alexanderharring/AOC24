l1 = []
l2 = []

with open("input.txt") as files:

    for line in files:

        x = line.strip().split()

        l1.append(int(x[0]))
        l2.append(int(x[1]))

s = 0
l1.sort()
l2.sort()
for z in range(len(l2)):
    s += abs(l1[z] - l2[z])

print(s)