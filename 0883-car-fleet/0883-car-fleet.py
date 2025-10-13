class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position,speed))[::-1]
        stack = []
        for p,s in pair:
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
            




       
