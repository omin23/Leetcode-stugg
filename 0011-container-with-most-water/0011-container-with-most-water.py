class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        max_length = 0 
        while l < r:
            max_length_curr = (r-l) * min(height[r],height[l])
            if height[r] > height[l]:
                l += 1
            elif height[r] < height[l]:
                r -= 1 
            else:
                r -= 1
            # print((l,r),(height[l],height[r]),max_length_curr)
            max_length = max(max_length_curr,max_length)
        
        return max_length
            
            
