class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        n=0
        for i in range(len(intervals)):
            i = i-n
            # print(i)
            if i < len(intervals) - 1 and intervals[i][1] >= intervals[i+1][0]:
                # print(i,n)
                intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
                intervals.pop(i+1)
                n+=1
            # print(intervals)
        return intervals
        