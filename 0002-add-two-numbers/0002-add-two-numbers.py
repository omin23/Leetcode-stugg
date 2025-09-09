# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        origin = ListNode(0)
        past = origin
        while l1 or l2:
            if not l1:
                ov = 0
            else:
                ov = l1.val
            if not l2: 
                tv = 0 
            else:
                tv = l2.val
            use = ov+tv+carry
            if use > 9:
                use = use - 10
                carry = 1 
            else:
                carry = 0
            new = ListNode(use)
            past.next = new
            past = new
            if l1:
                l1 = l1.next
                # print(l1)
            if l2:
                l2 = l2.next
                # print(l2)
        
        if carry:
            new = ListNode(1)
            past.next = new
        return origin.next