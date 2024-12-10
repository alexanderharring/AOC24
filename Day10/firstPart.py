lines = []

with open("input.txt") as files:
    for line in files:
        lines.append([int(z) for z in list(line.strip())])

visited = set()

n = 0

def track(pos):
    global n
    
    if pos not in visited:
        visited.add(pos)
        
        C = lines[pos[0]][pos[1]]
        
        if C == 9:
            n += 1
        
        for x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            
            np = (pos[0] + x[0], pos[1] + x[1])
            
                
            if np[0] < 0 or np[1] < 0 or np[0] >= len(lines) or np[1] >= len(lines[0]):
                continue
            
            if lines[np[0]][np[1]] - C == 1:
                track(np)
                
                
for i in range(len(lines)):
    for j in range(len(lines[0])):
        visited = set()
        if lines[i][j] == 0:
            track((i, j))
            
print(n)
