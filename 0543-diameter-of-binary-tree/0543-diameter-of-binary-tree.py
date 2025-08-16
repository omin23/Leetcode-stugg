# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = [0] 
        if not root: 
            return 0 

        self.calccir(root,maxd)

        return maxd[0]

    def calccir(self,node, maxd):
        if not node:
            return 0 
        
        ll = self.calccir(node.left,maxd)
        rl = self.calccir(node.right,maxd)

        d = (ll + rl) 
        if d > maxd[0]:
            maxd[0] = d

        return 1 + max(ll,rl) 


        