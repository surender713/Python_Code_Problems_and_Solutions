# Approach 1: Full Reversal

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


# Approach 2: Half Reversal (Optimized)

def isPalindrome(number):
    # Handle edge cases
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_half = 0

    while number > reversed_half:
        digit = number % 10
        reversed_half = reversed_half * 10 + digit
        number //= 10

    return number == reversed_half or number == reversed_half // 10