class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lf,ri = 0,len(numbers)-1
        while ri > lf:
            sum = numbers[lf] + numbers[ri]
            if sum == target:
                return[lf+1,ri+1]
            if sum > target:
                ri -=1
            else:
                lf += 1

        return[lf,ri+1]