# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(root,subroot):
            if not root and not subroot: 
                return True 
            if (not root and subroot) or (not subroot and root): 
                return False 
            if root.val != subroot.val:
                return False
            return issame(root.right,subroot.right) and issame(root.left,subroot.left) 
        
        def htree(root):
            if not root:
                return False
            if issame(root,subRoot):
                return True
            return htree(root.left) or htree(root.right) 

        return htree(root)

            