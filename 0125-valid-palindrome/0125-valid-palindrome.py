class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # print(s)
        new_str = ""
        for i in s:
            if i.isalpha():
                new_str += i
        print(new_str)
        length = len(new_str)
        for i in range(length//2):
            # print(new_str[i])
            # print(new_str[length-1-i])
            if new_str[i] != new_str[length-1-i]:
                return False

        return True 


        