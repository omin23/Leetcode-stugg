class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 

        totalwater = 0 
        l,r = 0,len(height)-1
        MaxL, MaxR = height[l],height[r]

        while l < r: 
            if MaxR > MaxL:
                l += 1
                MaxL = max(MaxL,height[l])
                totalwater += MaxL - height[l]
            else:
                r -= 1
                MaxR = max(MaxR,height[r])
                totalwater += MaxR - height[r]
        return totalwater


            
            


        return totalwater


        