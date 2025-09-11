from collections import defaultdict 

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.l1 = nums1
        self.l2 = nums2
        self.l2set = defaultdict(list)
        for i in enumerate(nums2):
            pos,val = i 
            self.l2set[val].append(pos)
        


    def add(self, index: int, val: int) -> None:
        old = self.l2[index]
        self.l2[index] += val
        self.l2set[old].remove(index)
        self.l2set[self.l2[index]].append(index)



    def count(self, tot: int) -> int:
        ret = 0 
        usearr = self.l1
        for i in usearr:
            l2maybe = tot-i
            if l2maybe in self.l2set.keys(): ret += len(self.l2set[l2maybe])

        return ret


        

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)