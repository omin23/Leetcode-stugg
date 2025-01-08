# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = [0]
        tar = [targetSum]
        if not root:
            return False
        
        def getp(root):
            print(sum[0])
            if not root.right and not root.left: 
                sum[0] += root.val
                print(sum[0])
                if sum[0] == tar[0]:
                    return True 
                sum[0] -= root.val
                return False
            sum[0] += root.val
            lc, rc = False, False
            if root.right:
                rc = getp(root.right)
            if rc == True:
                return True 
            if root.left:
                lc =  getp(root.left)
            sum[0] -= root.val
            return lc or rc

            
        
        
        return getp(root)
 

        