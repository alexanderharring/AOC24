import re

with open("input.txt") as files:
    
    data = files.read()
    
    x = re.findall("mul\(-?\d+,\-?\d+\)", data)
    
    bigsum = 0
     
    for z in x:
        
        nms = [int(p) for p in z[4:-1].split(",")]
        
        bigsum += nms[0] * nms[1]
        
    print(bigsum)
   
    