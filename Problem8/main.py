def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] < nums[end]:
                end = mid

            elif nums[mid] > nums[end]:
                start = mid + 1

            else:
                end -= 1
                
        return nums[start]