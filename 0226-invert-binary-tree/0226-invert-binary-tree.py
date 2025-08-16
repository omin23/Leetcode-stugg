# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            new = queue.popleft()
            if new.left:
                queue.append(new.left)
            if new.right:
                queue.append(new.right)
            
            new.left, new.right = new.right, new.left
        
        return root




        
        return root
