from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for i in strs:
            new = tuple(sorted(i))
            word_dict[new].append(i)
        res = list(word_dict.values())
        return res


         