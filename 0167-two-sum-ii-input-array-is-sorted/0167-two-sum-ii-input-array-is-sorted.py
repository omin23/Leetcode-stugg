class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0 
        res = numbers[right] + numbers[left]
        while res != target:
            if res > target: 
                right -=1
            elif res < target: 
                left +=1
            res = numbers[right] + numbers[left]
        return[left+1,right+1]







        
        
        
        # right_pointer = len(numbers)-1
        # left_pointer = 0 
        # while right_pointer > left_pointer: 
        #     if numbers[right_pointer] + numbers[left_pointer] > target:
        #         right_pointer -= 1
        #     elif numbers[right_pointer] + numbers[left_pointer] < target:
        #         left_pointer += 1
        #     else:
        #         break
        # return [left_pointer+1,right_pointer+1]