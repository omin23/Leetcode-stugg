# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        good = [True]
        def order(p,q):
            if (not p and q) or (not q and p) :good[0] = False
            if not p and not q: return 
            if not good[0]: return False
            if p.val == q.val:
                order(p.right,q.right)
                order(p.left,q.left)
            else: good[0] = False
        order(p,q)
        return good[0] 

        
