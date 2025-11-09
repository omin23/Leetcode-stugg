# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # nieve solution O(n) + O(nlogn)
        # res = []
        # if not root: return res
        
        # def dfs(root):
        #     if not root: return 
        #     res.append(root.val)
        #     dfs(root.right)
        #     dfs(root.left)
        
        # dfs(root)
        # res = sorted(res)
        # return res[k-1]
        res = []
        if not root: return res
        def dfs(root,k):
            if not root: return 
            # if len(res) == k: return 
            dfs(root.left,k)
            if len(res) == k: return 
            res.append(root.val)
            dfs(root.right,k)
        dfs(root,k)
        print(res)
        return res[-1]
