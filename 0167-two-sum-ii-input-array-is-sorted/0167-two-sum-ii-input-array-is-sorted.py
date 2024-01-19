class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lf,ri = 0,len(numbers)-1
        while ri > lf:
            sum = numbers[lf] + numbers[ri]
            
            if sum > target:
                ri -=1
            elif sum < target:
                lf += 1
            else:
                return[lf+1,ri+1]
        return