# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        good = [True]
        def dfs(root):
            if not root: return False
            if not good[0]: return False
            r = dfs(root.right)
            l = dfs(root.left)
            if abs(r-l) > 1: good[0] = False
            return 1 + max(l,r)
        dfs(root)
        return good[0]

        