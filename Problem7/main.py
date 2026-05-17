
def FindMin(nums):
    
    l =[0]

    for i in nums:
        for j in nums[::-1]:
            if i >= j:
                l.pop()
                l.append(j)
    
    return l[0]

        
def FindMin(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        
        if nums[mid] < nums[end]:
            end = mid
            
        else:
            start = mid + 1
            
    return nums[start]
    

       


FindMin([3,4,5,1,2])
FindMin([2,6,3])
FindMin([1])
FindMin([11,13,15,17])


