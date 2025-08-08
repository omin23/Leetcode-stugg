class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        max_length = 0 
        while l < r:
            max_length_curr = (r-l) * min(height[r],height[l])
            max_length = max(max_length_curr,max_length)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_length
            
            
