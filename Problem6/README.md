### problem

You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.

 * Note: A permutation of integers represents an arrangement of these numbers.

 

# Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.

# Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.

# Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.
 

## Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200


### Solutions

## 1. Adjacent Check Approach

# Idea:

* Sort the array
* Check if length is `n + 1`
* Ensure the largest element appears twice
* Verify that only the last two elements are duplicates

# Code:

```python
def isGood(nums):
    
    max_num = max(nums)
    length = len(nums)
    nums.sort()

    if (max_num + 1) == length:
        if nums.count(nums[-1]) == 2:
            for i in range(length):
                if nums[i] == nums[i+1]:
                    if i == length - 2:
                        return True
                    return False
        else:
            return False
    else:
        return False
````

## Complexity Analysis

* Time: **O(n log n)** (sorting) + **O(n)** (traversal)
* Space: **O(1)**

## 2. Counting-Based Approach

# Idea:

* Sort the array
* Check if length is `n + 1`
* Ensure:

  * Maximum element appears twice
  * All other elements appear exactly once

# Code:

```python
def isGood(nums):
        
    max_num = max(nums)
    length = len(nums)
    nums.sort()

    if ((max_num + 1) == length) and (nums.count(max_num) == 2):
        for i in nums[:-2]:
            if nums.count(i) != 1:
                return False
        return True
    else:
        return False
```



## Complexity Analysis

* Time: **O(n²)** (due to repeated `count()` calls)
* Space: **O(1)**



## Key Takeaways

* Array length must be exactly `n + 1`
* Maximum element determines `n`
* Only the largest element should appear twice
* All other elements must appear exactly once
* Sorting simplifies validation logic



## Summary

* Check array length
* Verify frequency of elements
* Ensure correct structure of `base[n]`


