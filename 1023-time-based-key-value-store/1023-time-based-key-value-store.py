from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.main = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.main[key] and self.main[key][-1][1] == value: return
        self.main[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        find = self.main[key]
        if not find: return ""
        idx = bisect_right(find,timestamp, key=lambda item:item[0]) - 1
        if idx >= 0: return find[idx][1]
        return ""




        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)