# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        good = [True]
        def mdfs(root):
            if not root or not good[0]:
                return 0
            rl = mdfs(root.right)
            ll = mdfs(root.left)

            if abs(rl - ll) > 1:
                good[0] = False
            return 1 + max(rl,ll)
        mdfs(root)
        return good[0]       

        