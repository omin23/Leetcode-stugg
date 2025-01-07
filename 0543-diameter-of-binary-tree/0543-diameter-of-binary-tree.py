# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = [0]

        def hi(root):
            if not root: 
                return 0

            lr = hi(root.left)
            rr = hi(root.right)

            dia = lr + rr

            maxd[0] = max(maxd[0],dia)
            
            return 1 + max(lr,rr)
    
        hi(root)
        return maxd[0]

        