# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(lc, rc):
            if not rc and not lc:
                return True 
            elif not rc or not lc:
                return False
            elif rc.val != lc.val:
                return False 
            
            return check(lc.right,rc.left) and check(lc.left,rc.right)
        
        return check(root,root)
        