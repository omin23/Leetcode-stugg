class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        a = sorted(a)
        print(a)
        if len (a) > 1:
            for i in range(len(a)):
                if(a[i-1] == a[i]):
                    return True
        return False