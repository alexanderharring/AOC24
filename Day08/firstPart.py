lines = []

data = {}
antinodeCount = 0
with open("input.txt") as files:
    
    
    for line in files:
        
        lines.append(line.strip())

for i in range(len(lines)):
    for j in range(len(lines[0])):

        c = lines[i][j]

        if c != ".":

            if c not in data:

                data[c] = []

            data[c].append((i, j))

def calculateAntiPair(p0, p1):

    ds = (p1[0]-p0[0], p1[1]-p0[1])

    P2 = (p1[0] + ds[0], p1[1] + ds[1])
    P3 = (p0[0] - ds[0], p0[1] - ds[1])

    return (P2, P3)


def isInBounds(p):

    if p[0] < 0 or p[1] < 0 or p[0] >= len(lines) or p[1] >= len(lines[0]):
        return False
    
    return True

checkSet = set()

for k in data.keys():

    posns = data[k]
    for i in range(len(posns)-1):
        for j in range(i+1, len(posns)):

            (A0, A1) = calculateAntiPair(posns[i], posns[j])

            if isInBounds(A0):
                checkSet.add(A0)

            if isInBounds(A1):
                checkSet.add(A1)


print(len(checkSet))
            

