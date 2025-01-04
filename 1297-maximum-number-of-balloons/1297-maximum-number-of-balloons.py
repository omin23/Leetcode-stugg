from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        count["l"] =  count["l"]//2
        count["o"] = count["o"]//2

        return min(count["b"],count["a"],count["l"],count["o"],count["n"])

        # res = 0 
        # while (count["b"] > 0 
        #         and count["a"] > 0 and count["l"] > 1
        #         and count["o"] > 1 and count["n"] > 0):
        #     res +=1
        #     count["b"] -= 1 
        #     count["a"] -= 1 
        #     count["l"] -= 2
        #     count["o"] -= 2 
        #     count["n"] -= 1 
        return res