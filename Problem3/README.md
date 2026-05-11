### Problem:-

Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

# Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

## Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

### Solutions

## 1. Brute Force Approach (O(n²) + extra space)

# Idea:

* Generate all substrings starting from each index
* Store valid substrings (no duplicates)
* Return maximum length

# Code:

``` python

def lengthOfLongestSubstring(s):
    
    l = []  # store substrings without repeating characters
    
    for i in range(len(s)):
        x = ""
        
        for j in range(i, len(s)):
            if s[j] not in x:
                x += s[j]
            else:
                break
        
        l.append(x)
    
    los = []
    for i in l:
        los.append(len(i))
    
    if los:
        return max(los)
    else:
        return 0
```


# Complexity:

* Time: O(n²)
* Space: O(n²)

-

## 2. Improved Brute Force , optimized space

# Idea:

* No need to store all substrings
* Track maximum length directly

# Code:

```python
def lengthOfLongestSubstring(s):
    
    max_len = 0
    
    for i in range(len(s)):
        x = ""
        
        for j in range(i, len(s)):
            if s[j] not in x:
                x += s[j]
                max_len = max(max_len, len(x))
            else:
                break
    
    return max_len
```

# Complexity:

* Time: O(n²)
* Space: O(1) 


## 3. Optimal Approach — Sliding Window 

# Idea:

* Use a window with two pointers (`left`, `right`)
* Maintain a set of unique characters
* Expand window when valid
* Shrink when duplicate appears

# Code:

```python
def lengthOfLongestSubstring(s):
    
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```



## Complexity Comparison

| Approach             | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Brute Force          | O(n²)           | O(n²)            |
| Improved Brute Force | O(n²)           | O(1)             |
| Sliding Window       | O(n)            | O(n)             |



## Key Takeaways

* Avoid recomputing substrings repeatedly
* Use **two pointers + set** for optimal performance
* Sliding window is a common pattern in string problems


## Summary

* Start with brute force to understand the problem
* Optimize step-by-step
* Aim for **O(n)** using sliding window

