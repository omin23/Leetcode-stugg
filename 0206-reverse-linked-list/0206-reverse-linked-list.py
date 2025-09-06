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
        present = head.next
        future = head.next.next
        past.next = None

        while future:
            present.next = past
            past = present 
            present = future 
            future = future.next 
        present.next = past
        return present 



        