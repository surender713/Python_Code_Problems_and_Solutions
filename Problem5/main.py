# 1. Mathematical Approach (Digit Extraction)

def reverse(x):
       
    original_number = x
    x = abs(x)
    reversed_number = 0

    while x:
        digit = x % 10
        reversed_number = (reversed_number * 10) + digit
        x = x // 10
        
    if -2147483648 <= reversed_number <= 2147483647:
                
        if original_number < 0:
            return  -1 * reversed_number
            
        return reversed_number 
    else:
        return 0


# 2. String-Based Approach

def reverse(x):
        sign = -1 if x < 0 else 1
        reversed_number  = int(str(abs(x))[::-1]) * sign

        if reversed_number  < -2147483648 or reversed_number  > 2147483647:
            return 0

        return reversed_number