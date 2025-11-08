# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [[root.val]]
        record = deque([root])
        new = []
        while record or new: 
            if not record: 
                vals = [i.val for i in new]
                res.append(vals)
                record = deque(new)
                new = []
            use = record.popleft()
            if use.left: new.append(use.left)
            if use.right: new.append(use.right)
        
        print(res)
        return res 


