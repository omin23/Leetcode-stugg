"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        maxval = [1]

        def moddfs(curval,root):
            for i in root.children:
                moddfs(curval+1,i)
                maxval[0] = max(curval+1,maxval[0])
        
        moddfs(1,root)
        return maxval[0]

        