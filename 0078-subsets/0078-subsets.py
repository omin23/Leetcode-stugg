class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        print(n)
        def bt(i):
            if i == n: 
                res.append(sol[:])
                return 
            
            bt(i+1)
            sol.append(nums[i])
            bt(i+1)
            sol.pop()
            return 
        bt(0)
        return res 

        