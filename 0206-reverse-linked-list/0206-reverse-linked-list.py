# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        past = head
        now = past.next
        future = now.next
        past.next = None
        while future:
            now.next = past
            past = now
            now = future
            future = now.next
            
        now.next = past
        return now



        