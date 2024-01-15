class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for index,value in enumerate(nums):
            num = target-value
            if (num) in map:
                return [map[num],index]
            map[value] = index 
        return
            
        