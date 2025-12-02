from collections import Counter 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        # print(count)
        num = 0
        for i in range(3):
            j = count[i]
            for k in range(num,num+j): nums[k] = i
            num += j
        return nums

