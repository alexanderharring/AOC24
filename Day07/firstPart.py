lines = []
with open("input.txt") as files:
    
    
    for line in files:
        
        c = line.strip().split(":")
        k = int(c[0])
        n = [int(p) for p in c[1].split()]
        
        lines.append([k, n])

bigSum = 0
        
for maybeLine in lines:
    
    target = maybeLine[0]
    nums = maybeLine[1]
    
    solved = False

    def otherTrack(target, nums):
        if target == 1 or target == 0:
            return True
        if len(nums) == 0:
            return
        
        lastN = nums[-1]
        
        if (target % lastN) == 0:
            if otherTrack(int(target / lastN), nums[:-1]):
                return True
            
        if otherTrack(target - lastN, nums[:-1]):
            return True
        

    res = otherTrack(target, nums)
    
    if res:
        bigSum += target
        
print(bigSum)
        
    