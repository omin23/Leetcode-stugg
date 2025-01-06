class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = total = sum(nums[:k])
        it = len(nums) - k 
        for i in range(it):
            total += nums[k+i] - nums[i] 
            avg = max(avg,total)
        return avg/k

            

