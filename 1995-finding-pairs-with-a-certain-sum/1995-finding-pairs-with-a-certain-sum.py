from collections import Counter 

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.l1 = nums1
        self.l2 = nums2
        self.l1set = Counter(nums1)
        self.l2set = Counter(nums2)        


    def add(self, index: int, val: int) -> None:
        old = self.l2[index]
        self.l2[index] += val
        self.l2set[old] -= 1
        self.l2set[self.l2[index]] += 1



    def count(self, tot: int) -> int:
        ret = 0 
        for i in self.l1set.items():
            val , it = i 
            l2maybe = tot-val
            if l2maybe in self.l2set.keys(): ret += it * self.l2set[l2maybe]

        return ret


        

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)