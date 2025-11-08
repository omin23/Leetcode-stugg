# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        cur = [0]
        def dfs(root, val): 
            if not root: return 
            if cur[0] == val: 
                res.append(root.val)
                cur[0] += 1
            dfs(root.right,val+1)
            dfs(root.left, val+1)

        dfs(root,0)
        return res

