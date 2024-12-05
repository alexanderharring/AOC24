import math

dataOne = []
dataTwo = []

with open("input.txt") as files:
    
    for line in files:
        
        splitted = line.split("|")
        
        if line.isspace():
            continue
        
        if len(splitted) > 1:
            
            data = [int(x) for x in splitted]
            
            dataOne.append((data[0], data[1]))
        else:
            
            
            newSplit = line.strip().split(",")
            
            dataTwo.append([int(x) for x in newSplit])
            
doubleMap = {}
for pairs in dataOne:
    
    if pairs[0] not in doubleMap:
        doubleMap[pairs[0]] = set()
        
    doubleMap[pairs[0]].add(pairs[1])

bigSum = 0
hl = []
for ind, line in enumerate(dataTwo):
    
    seen = set()
    
    good = True
    for book in line:
        
        if good==False:
            break
        
        
        if book in doubleMap:
            
            otherPair = doubleMap[book]
            
            if len(seen.intersection(otherPair)) > 0:
                
                hl.append(ind)
                break
            
        seen.add(book)

for i,l in enumerate(dataTwo):
    
    if i not in hl:
        bigSum += l[int(math.floor(len(l)/2))]
        
print(bigSum)
        
        