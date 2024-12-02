
with open("input.txt") as files:

    count = 0

    for line in files:

        data = [int(x) for x in line.strip().split()]

        lineCorrect = True

        for i in range(1, len(data)):

            dt = data[i] - data[i-1]

            if abs(dt) < 1 or abs(dt) > 3:

                lineCorrect = False 
                break

            if (i != 1):

                parity = (data[i-1] - data[i-2]) / abs((data[i-1] - data[i-2]))
                
                if parity*data[i] <= parity*data[i-1]:
                    lineCorrect = False 
                    break
        
        if lineCorrect:
            count += 1

    print(count)