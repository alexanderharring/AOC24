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

    return (P2, P3), ds


def isInBounds(p):

    if p[0] < 0 or p[1] < 0 or p[0] >= len(lines) or p[1] >= len(lines[0]):
        return False
    
    return True

def extend(dt):

    newPositions = []


checkSet = set()

for k in data.keys():

    posns = data[k]
    for i in range(len(posns)-1):
        for j in range(i+1, len(posns)):

            (A0, A1), ds = calculateAntiPair(posns[i], posns[j])

            checkSet.add(posns[i])
            checkSet.add(posns[j])

            while isInBounds(A0):

                checkSet.add(A0)
                A0 = (A0[0] + ds[0], A0[1] + ds[1])

            while isInBounds(A1):

                checkSet.add(A1)
                A1 = (A1[0] - ds[0], A1[1] - ds[1])


print(len(checkSet))
            

