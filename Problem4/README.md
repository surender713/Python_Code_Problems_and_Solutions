### Problem

Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

## Constraints:

-231 <= x <= 231 - 1




### Approach 1: Full Reversal

## Idea

Reverse the entire number and compare it with the original number.

## Code

```python
def isPalindrome(number):
    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10

    return reversed_number == original_number
```

### Complexity

* Time Complexity: O(n)
* Space Complexity: O(1)



### Approach 2: Half Reversal (Optimized)

## Idea

Instead of reversing the whole number, reverse only half of it and compare both halves.

## Key Observations

* Negative numbers are not palindromes
* Numbers ending in 0 (but not 0 itself) are not palindromes

## Code

```python
def isPalindrome(number):
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_half = 0

    while number > reversed_half:
        digit = number % 10
        reversed_half = reversed_half * 10 + digit
        number //= 10

    return number == reversed_half or number == reversed_half // 10
```

### Complexity

* Time Complexity: O(n)
* Space Complexity: O(1)


## Summary

* Both approaches solve the problem efficiently.
* The half-reversal method is preferred in interviews due to reduced operations.
* No string conversion is used, ensuring optimal space usage.


