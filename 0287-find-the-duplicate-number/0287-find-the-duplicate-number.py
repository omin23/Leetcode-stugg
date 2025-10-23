class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums: 
            # if the number is already negative then we terminate
            if nums[abs(i)-1] < 0: return abs(i)
            # Make it  negative 
            nums[abs(i)-1] *= -1
        return 