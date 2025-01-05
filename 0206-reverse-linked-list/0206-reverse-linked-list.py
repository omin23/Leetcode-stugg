# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fr = head
        prev = None

        while fr: 
            nxt = fr.next
            fr.next = prev  
            prev = fr           
            fr = nxt
            
        return prev



