# 1. Brute Force Approach (O(n²) + extra space)

def lengthOfLongestSubstring(s):
    
    l = []  # list to store all valid substrings without repeating characters
    
    # loop through each starting index of the string
    for i in range(len(s)):
        x = ""  # current substring
        
        # build substring starting from index i
        for j in range(i, len(s)):
            # if character not already in substring, add it
            if s[j] not in x:
                x += s[j]
            else:
                # duplicate found → stop expanding this substring
                break
        
        # store the substring formed from index i
        l.append(x)
    
    los = []  # list to store lengths of substrings
    
    # calculate length of each substring
    for i in l:
        los.append(len(i))
    
    # print maximum length if list is not empty
    if los:
        return max(los)
    else:
        # if input string is empty
        return 0


# 2. Improved Brute Force , optimized space

def lengthOfLongestSubstring(s):
    
    max_len = 0  # track maximum length
    
    for i in range(len(s)):
        x = ""
        
        for j in range(i, len(s)):
            if s[j] not in x:
                x += s[j]
                max_len = max(max_len, len(x))  # update here
            else:
                break
    
    return max_len


## 3. Optimal Approach — Sliding Window 

def lengthOfLongestSubstring(s):
    
    char_set = set()  # store current window characters
    left = 0          # left pointer of window
    max_len = 0       # result
    
    # expand window using right pointer
    for right in range(len(s)):
        
        # if duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # add current character
        char_set.add(s[right])
        
        # update max length
        max_len = max(max_len, right - left + 1)
    
    return max_len