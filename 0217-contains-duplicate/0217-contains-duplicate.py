class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        map = set()
        for n in a:
            if n in map:
                return True
            map.add(n)
        return False