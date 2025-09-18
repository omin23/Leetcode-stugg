class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        useable_1 = k 
        maxnum = 0 
        curr = 0 
        l1,l2 = -1,0
        if not nums:
            return 0 
        
        while l1 < len(nums)-1:
            l1 += 1
            if nums[l1] == 1: curr +=1
            elif useable_1: useable_1,curr = useable_1 - 1 , curr+1
            else:
                maxnum = max(maxnum,curr)
                while not useable_1:
                    if nums[l2] == 0:
                        useable_1 += 1
                    curr -=1
                    l2 += 1
                l1-=1
        maxnum = max(maxnum,curr)         
        return maxnum



