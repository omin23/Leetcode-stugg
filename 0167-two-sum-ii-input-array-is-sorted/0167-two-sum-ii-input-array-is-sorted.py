class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_pointer = len(numbers)-1
        left_pointer = 0 
        while right_pointer > left_pointer: 
            if numbers[right_pointer] + numbers[left_pointer] > target:
                right_pointer -= 1
            elif numbers[right_pointer] + numbers[left_pointer] < target:
                left_pointer += 1
            else:
                break
        return [left_pointer+1,right_pointer+1]