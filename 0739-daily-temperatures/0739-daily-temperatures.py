class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        if length == 1: return [0]
        res = [0 for _ in range(length)]
        s = []
        s.append(0)
        for i in range(1,length):
            # print(s[-1],temperatures[s[-1]],temperatures[i])
            while s and temperatures[s[-1]] < temperatures[i]:
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return res


