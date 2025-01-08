class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = combinations(nums,k)
        final = [list(i) for i in res]
        return final 

        # sol, res = [],[]
        # def bt(j):
        #     if len(sol) == k:
        #         res.append(sol[:])
        #         return

        #     for j in range(j,n):
        #         sol.append(nums[j])
        #         bt(j+1)
        #         sol.pop()
        #     return       
        
        # bt(0)
        return res 