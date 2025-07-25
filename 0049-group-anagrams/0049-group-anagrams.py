from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_mapper = defaultdict(list)
        
        for i in strs:
            word_mapper[tuple(sorted(i))].append(i)
        
        res = []
        for i in word_mapper.values():
            res.append(i)

        return res


         