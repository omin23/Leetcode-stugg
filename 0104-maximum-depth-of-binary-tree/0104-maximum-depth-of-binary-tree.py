# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.right and root.left:
            return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1 
        elif root.right: 
            return self.maxDepth(root.right) + 1
        return self.maxDepth(root.left) + 1


        