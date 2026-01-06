class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        check = {0:1}
        total = 0 
        res = 0 
        for i in nums: 
            total += i
            diff = total - k

            if diff in check.keys(): res += check[diff]            
            check[total] = check.get(total,0) + 1

        return res