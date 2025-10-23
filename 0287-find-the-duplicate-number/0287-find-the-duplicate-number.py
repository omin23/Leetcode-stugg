class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums: 
            # if the number is already negative then we terminate
            idx = abs(i)-1
            if nums[idx] < 0: return abs(i)
            # Make it  negative 
            nums[idx] *= -1
        return 