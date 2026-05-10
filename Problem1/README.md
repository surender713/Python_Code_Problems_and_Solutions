Problem:-

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Solutions:-

1st Attempt (Brute Force)

"""
def twosum(nums, target):    
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                if i != j:
                  return [i,j]
"""    


Try every possible pair of elements
Checks if their sum equals target
Simple but inefficient

Complexity
Time: O(n²)
Space: O(1)

2nd Attempt (Optimal - Hash Map)

"""
def twoSum(nums, target):
    d = {}
    for i, x in enumerate(nums):
        if target - x in d: return [d[target - x], i]
        d[x] = i
"""

Store elements in a dictionary as you iterate
For each number x, compute target - x (complement)
If complement already exists → pair found instantly
Avoids re-checking previous elements

Complexity
Time: O(n)
Space: O(n)

Key Improvement: Instead of checking all pairs, we find the answer in one pass using a hash map.