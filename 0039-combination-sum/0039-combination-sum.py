class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [],[]
        n = len(candidates)

        def bt(i,tar):
            if tar < 0 or i == n:
                return
            elif tar == 0: 
                res.append(sol[:])
                return 

            #pick 
            sol.append(candidates[i])
            bt(i,tar-candidates[i])
            sol.pop()

            #not pick 
            bt(i+1,tar)
            return 
        bt(0,target)
        return res