# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdept = [0]
        def dfs(root):
            if not root: 
                return 0
            rl = dfs(root.right)
            ll = dfs(root.left)
            
            maxdept[0] = max(maxdept[0],rl+ll)

            return 1 + max(ll,rl)
        dfs(root)
        
        return maxdept[0]
        

   
        