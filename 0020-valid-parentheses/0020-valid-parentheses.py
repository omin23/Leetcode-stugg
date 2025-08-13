class Solution:
    def isValid(self, s: str) -> bool:

        close_dict = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        storage = []

        for i in s:
            if i in close_dict.keys():
                if not storage: 
                    return False
                if close_dict[i] == storage[-1]:
                    storage.pop()
                else: 
                    return False
            else:
                storage.append(i)
        
        if storage:
            return False
        return True 