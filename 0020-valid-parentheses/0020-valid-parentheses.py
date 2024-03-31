class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = {')':'(','}':'{',']':'['}
        
        for i in s:
            if i in cto:
                if stack and cto[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(i)
        return not stack 
        