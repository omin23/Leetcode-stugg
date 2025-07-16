class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lib = set()
        for i in nums: 
            if i in lib: 
                return True 
            else: 
                lib.add(i)
        return False 