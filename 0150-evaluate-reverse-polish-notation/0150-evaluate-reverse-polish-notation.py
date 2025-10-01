class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2: return int(tokens[0])
        nums = []
        for i in range(len(tokens)): 
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                nums.append(tokens[i])
            else:
                # print(nums)
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                op = tokens[i]
                # print(op)
                if op == "+": 
                    # print(num2,op,num1)
                    nums.append(num1 + num2)
                elif op == "-":
                    # print(num2,op,num1)
                    nums.append(num2 - num1)
                elif op == "*": 
                    # print(num2,op,num1)
                    nums.append(num1 * num2)
                else: 
                    # print(num2,op,num1)
                    nums.append(int(num2 / num1))  

        # for i in opers: 
        #     print(nums, opers)
        #     num1 = int(nums.pop())
        #     num2 = int(nums.pop())
        #     op = opers.pop()
            
        return nums[0]