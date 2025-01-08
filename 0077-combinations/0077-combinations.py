class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        print(nums)
        sol, res = [],[]
        def bt(i,j):
            if i == k:
                res.append(sol[:])
                return

            for j in range(j,n):
                sol.append(nums[j])
                bt(i+1,j+1)
                sol.pop()
            return       
        
        bt(0,0)
        return res 