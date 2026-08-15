class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mapd = {0:1}
        value = 0 
        for i in nums:
            value += i 
            if value-k in mapd.keys(): res += mapd[value-k]
            mapd[value] = mapd.get(value,0) + 1
        return res


