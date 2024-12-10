import math

board = []
with open("input.txt") as files:
    
    
    for line in files:
        
        board.append(line.strip())
        
guardPos = (-1, -1)    
guardDirection = "^"
    
for i in range(len(board)):
    for j in range(len(board[0])):
        
        if board[i][j] == "^":
            guardPos = (i, j)

directionMap = {}
directionMap["v"] = (1, 0)
directionMap["^"] = (-1, 0)
directionMap[">"] = (0, 1)
directionMap["<"] = (0, -1)

cycle = ["^", ">", "v", "<"]
cyclePos = 0

visited = set()
visited.add(guardPos)

def happy(p):
    return p[0] < len(board) and p[1] < len(board[0]) and p[0] >= 0 and p[1] >= 0

while happy(guardPos):
    
    nextPos = (guardPos[0] + directionMap[guardDirection][0], guardPos[1] + directionMap[guardDirection][1])
    
    if happy(nextPos) and board[nextPos[0]][nextPos[1]] == "#":
        cyclePos += 1
        guardDirection = cycle[cyclePos % 4]
    else:
        guardPos = nextPos
        visited.add(guardPos)
        
print(len(visited)-1)
        
        
        
    
    