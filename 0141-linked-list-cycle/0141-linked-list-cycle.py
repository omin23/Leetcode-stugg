# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lib = set()
        while head:
            if head not in lib:
                lib.add(head)
                head = head.next
            else: 
                return True 
        return False


        