# Adjacent Check Approach

def isGood(nums):
    
    max_num = max(nums)
    length = len(nums)
    nums.sort()

    if (max_num + 1) == length:
        if nums.count(nums[-1]) == 2 :
            for i in range(length):
                if nums[i] == nums[i+1]:
                    if i == length-2:
                        return True
                    return False
        else:
            return False
    else:
        return False
    
# Counting-Based Approach
    
def isGood(nums):
        
    max_num = max(nums)
    length = len(nums)
    nums.sort()

    if ((max_num + 1) == length) and (nums.count(max_num) == 2) :
        for i in nums[:-2]:
            if nums.count(i) != 1:
                return False
        return True
    
    else:
        return False
