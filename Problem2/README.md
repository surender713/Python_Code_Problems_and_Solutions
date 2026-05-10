Problem:-

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

![alt text](addtwonumber1.jpg)
 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Solurion:-

1st Attempt (String / Integer Conversion)

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    s1 = ""
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    
    s2 = ""
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    
    n1 = int(s1[::-1])
    n2 = int(s2[::-1])
    
    total = n1 + n2
    
    head = ListNode(0)
    pointer = head
        
    for digit in str(total)[::-1]:
        pointer.next = ListNode(int(digit))
        pointer = pointer.next
        
    return head.next
"""

Explanation
Convert linked list → string
Reverse → convert to integer
Add numbers
Convert result back → linked list

Complexity
Time: O(n)
Space: O(n)

2nd Attempt (Optimal - Carry Method)

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    head = ListNode(0)
    pointer = head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        
        pointer.next = ListNode(total % 10)
        pointer = pointer.next
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return head.next
"""

Explanation

Traverse both linked lists
Add digits one by one
Maintain a carry
Build result list dynamically
Complexity
Time: O(max(n, m))
Space: O(max(n, m))

Key Improvement:-

Instead of converting the entire number:

We simulate manual addition (digit by digit)
This avoids large integer conversions
Works efficiently for long linked lists