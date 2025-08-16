# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0 
            rl = dfs(node.right)
            ll = dfs(node.left)

            if abs(rl - ll) > 1:
                return float("infinity")
            return max(rl,ll) + 1
        
        d = dfs(root)

        if d == float("infinity"):
            return False
        return True

        