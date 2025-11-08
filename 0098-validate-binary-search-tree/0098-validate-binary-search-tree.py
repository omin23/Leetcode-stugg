# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        good = [True]
        def dfs(root,ll,ul):
            if not root: return 
            if not good[0]: return 
            if root.val <= ll or root.val >= ul:
                good[0] = False
                return 
            dfs(root.right,root.val,ul)
            dfs(root.left,ll,root.val)
        dfs(root,float("-inf"),float("inf"))
        return good[0] 
        