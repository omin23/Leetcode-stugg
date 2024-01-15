class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        map = {}
        for i,n in enumerate(a):
            if n in map:
                return True
            map[n] = i
        return False