def isSafe(inpt):
    deltas = [0] * (len(inpt)-1)

    for i in range(1, len(inpt)):
        deltas[i-1] = inpt[i] - inpt[i-1]


    for z in deltas:
        if abs(z) < 1:
            return False
        
        if abs(z) > 3:
            return False

    if sum([n>0 for n in deltas]) == len(inpt)-1 or sum([n<0 for n in deltas]) == len(inpt)-1:
        return True

    return False



with open("input.txt") as files:

    count = 0

    for line in files:
        data = [int(x) for x in line.strip().split()]

        if isSafe(data):
            count += 1
        else:
            for i in range(len(data)):
                
                newL = data.copy()
                newL.pop(i)

                if isSafe(newL):
                    
                    count += 1
                    break


    print(count)