class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



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