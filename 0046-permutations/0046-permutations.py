class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        def bt(i):
            if i == n:
                res.append(sol[:]) 
                return 
        
            for j in nums:
                if j not in sol:
                    sol.append(j)
                    bt(i+1)
                    sol.pop()
            return

        bt(0)
        return res
        