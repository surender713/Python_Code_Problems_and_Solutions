# 1st Attempt (Brute Force)

def twosum(nums, target):    
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                if i != j:
                  return [i,j]
    

# 2nd Attempt (Optimal - Hash Map)    

def twoSum(nums, target):
    d = {}
    for i, x in enumerate(nums):
        if target - x in d: return [d[target - x], i]
        d[x] = i