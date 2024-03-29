class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        m = {}
        lis = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            m[n] = 1 + m.get(n,0)
        for n,c in m.items():
            if n%2 == 0:
                lis[c].append(n)
        total_len = 0;
        for i in lis:
            total_len = total_len +len(i)
        for i in range(len(lis)-1,0,-1):
            if len(lis[i]) == 0:
                pass
            else:
                lis[i].sort()
                return lis[i][0]
        if (len(lis[1]) == total_len):
            return -1