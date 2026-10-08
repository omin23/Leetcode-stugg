class NumArray:

    def __init__(self, nums: list[int]):
        self.num = [nums[0]]
        for i in range(1,len(nums)): 
            self.num.append(self.num[i-1]+nums[i])
        print(self.num)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.num[right]
        return self.num[right] - self.num[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)