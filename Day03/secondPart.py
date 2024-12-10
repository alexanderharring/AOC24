import re

with open("input.txt") as files:
    
    data = files.read()
    
    x = re.findall("(mul\(-?\d+,\-?\d+\)|don't\(\)|do\(\))", data)
    
    bigsum = 0
    
    keep = True
    
    m = x[:]
    
    for z in x:
        
        if z == "don't()":
            keep = False
            m.remove(z)
        elif z == "do()":
            keep = True
            m.remove(z)
        else:
            
            if not keep:
                m.remove(z)
    
    
    for z in m:
        
        nms = [int(p) for p in z[4:-1].split(",")]
        
        bigsum += nms[0] * nms[1]
        
    print(bigsum)
   
    