### Problem:-

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

Input: x = 123
Output: 321

# Example 2:

Input: x = -123
Output: -321

# Example 3:

Input: x = 120
Output: 21

## Constraints:

-2³¹ ≤ x ≤ 2³¹ - 1

### Solutions:-

## 1. Mathematical Approach (Digit Extraction)

# Idea:

* Extract digits using modulo operation
* Build the reversed number step-by-step
* Keep track of the original sign
* Check if the result stays within 32-bit integer range

# Code:

```python
def reverse(x):
       
    original_number = x
    x = abs(x)
    reversed_number = 0

    while x:
        digit = x % 10
        reversed_number = (reversed_number * 10) + digit
        x = x // 10
        
    if -2**31 <= reversed_number <= 2**31 - 1:
                
        if original_number < 0:
            return -1 * reversed_number
            
        return reversed_number 
    else:
        return 0
```

# Complexity:

* Time: O(log n)
* Space: O(1)

---

## 2. String-Based Approach

# Idea:

* Convert the integer to a string
* Reverse the string
* Convert it back to an integer
* Reapply the original sign
* Validate against overflow constraints

# Code:

```python
def reverse(x):
    sign = -1 if x < 0 else 1
    reversed_number = int(str(abs(x))[::-1]) * sign

    if reversed_number < -2**31 or reversed_number > 2**31 - 1:
        return 0

    return reversed_number
```

# Complexity:

* Time: O(n)
* Space: O(n)


## Complexity Comparison

| Approach     | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Mathematical | O(log n)        | O(1)             |
| String-Based | O(n)            | O(n)             |


## Key Takeaways

* Always handle **overflow conditions carefully**
* Mathematical approach is more efficient than string-based in space
* Proper handling of negative numbers is essential


## Summary

* Start with reversing digits step-by-step
* Consider constraints like overflow
* Choose approach based on simplicity vs efficiency
