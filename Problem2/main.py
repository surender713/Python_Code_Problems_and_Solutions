class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#1st Attempt (String / Integer Conversion)

def addTwoNumbers(l1, l2):
    # Convert l1 to string
    s1 = ""
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    
    # Convert l2 to string
    s2 = ""
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    
    # Reverse and convert to int
    n1 = int(s1[::-1])
    n2 = int(s2[::-1])
    
    total = n1 + n2
    
    # Convert back to linked list
    head = ListNode(0)     
    pointer = head
        
    for digit in str(total)[::-1]:
        pointer.next = ListNode(int(digit))
        pointer = pointer.next
        
    return head.next


#2nd Attempt (Optimal - Carry Method)

def addTwoNumbers(l1, l2):
    head = ListNode(0)          # Dummy node to simplify result list creation
    pointer = head              # Pointer to build the new linked list
    carry = 0                   # Carry to handle sums >= 10
    
    while l1 or l2 or carry:    # Continue until both lists and carry are exhausted
        
        val1 = l1.val if l1 else 0   # Get value from l1 (0 if l1 is None)
        val2 = l2.val if l2 else 0   # Get value from l2 (0 if l2 is None)
        
        total = val1 + val2 + carry  # Sum current digits + carry
        carry = total // 10          # Update carry (e.g., 15 → carry = 1)
        
        pointer.next = ListNode(total % 10)  # Store last digit of total in new node
        pointer = pointer.next               # Move pointer to next node
        
        if l1: l1 = l1.next   # Move to next node in l1 if exists
        if l2: l2 = l2.next   # Move to next node in l2 if exists
    
    return head.next   # Return result list (skip dummy node)