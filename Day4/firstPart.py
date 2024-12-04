board = []

with open("input.txt") as files:
    
    for line in files:
        
        board.append(line.strip())
        
kernel = [["👿"]*4]*4



def checkKernal():
    bigCount = 0

    for i in range(4):
        
        w = ""
        for j in range(4):
            w += kernel[j][i]
            
        if w == "XMAS":
            bigCount += 1
        if w == "SAMX":
            bigCount += 1
            
            
    oneDiagonal = ""
    twoDiagonal = ""
    
    for i in range(4):
        if kernel[i] == "XMAS":
            bigCount += 1
            
        if kernel[i] == "SAMX":
            bigCount += 1
        
        oneDiagonal += kernel[i][i]
        twoDiagonal += kernel[3-i][i]
        
    if oneDiagonal == "XMAS":
        bigCount += 1
    
    if oneDiagonal == "SAMX":
        bigCount += 1
        
    if twoDiagonal == "XMAS":
        bigCount += 1
    
    if twoDiagonal == "SAMX":
        bigCount += 1
            
    return bigCount
            
massive = 0

for i in range(0, len(board)-3):
    for j in range(0, len(board[0])-3):
        
        for p in range(4):
            kernel[p] = board[i+p][j:j+4]
            
        dt = checkKernal()
        
        print("")
        print(kernel[0])
        print(kernel[1])
        print(kernel[2])
        print(kernel[3])
        print(dt)
        print("")
        
        
        massive += dt

print(massive)
        