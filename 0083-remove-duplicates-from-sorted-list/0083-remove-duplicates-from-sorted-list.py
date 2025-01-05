# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if head == None or curr.next == None: 
            return head
        while curr.next.next != None: 
            print(curr.val,curr.next.val)
            if curr.next.val == curr.val:
                temp = curr.next
                temp = None
                curr.next = curr.next.next
            else: 
                curr = curr.next
        if curr.next.val == curr.val:
                temp = curr.next
                temp = None
                curr.next = curr.next.next
            
        return head

            