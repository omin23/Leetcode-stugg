class Solution:
    def isValid(self, s: str) -> bool:

        cd = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        storage = []

        for i in s: 
            if i in cd.keys():
                if not storage: return False
                if cd[i] == storage[-1]: storage.pop()
                else: return False
            else: storage.append(i)

        if not storage: return True
        return False