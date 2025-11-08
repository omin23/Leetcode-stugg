# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = []
        goodn = [0]

        def dfs(root,maxn):
            if root.val >= maxn: goodn[0] += 1
            if root.right: dfs(root.right,max(maxn,root.right.val))
            if root.left: dfs(root.left,max(maxn,root.left.val))
            return 

        dfs(root,root.val)
        return goodn[0]