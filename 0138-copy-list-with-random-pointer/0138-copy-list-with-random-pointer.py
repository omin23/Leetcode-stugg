"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {}
        # first pass
        first = head
        newhad = Node(0)
        track = newhad
        mapper[None] = None
        while first:
            new = Node(first.val)
            mapper[first] = new
            track.next = new
            track = track.next
            first = first.next

        # second pass
        first = head
        track = newhad.next
        while first:
            track.random = mapper[first.random]
            track = track.next
            first = first.next



        return newhad.next
        
        






