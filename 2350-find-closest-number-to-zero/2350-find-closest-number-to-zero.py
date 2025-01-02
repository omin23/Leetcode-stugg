class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = 10000000000
        for i in nums: 
            new = abs(i)
            if new < abs(res):
                res = i
            elif new == abs(res) and res < i:
                res = i 

        return res 

