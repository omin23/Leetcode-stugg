# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root,subroot):
            if (not root and subroot) or (root and not subroot): return False
            if not root and not subroot: return True
            if root.val == subroot.val: 
                return same(root.left, subroot.left) and same(root.right,subroot.right)
            return False
        good = [False]
        def dfs(root,subroot):
            if not root: return False
            if good[0]: return True
            if root.val == subroot.val: good[0] = same(root,subroot)

            dfs(root.right, subroot)
            dfs(root.left, subroot)

            return good[0]

        return dfs(root,subRoot) 

        

            