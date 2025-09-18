from collections import defaultdict
from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.mapper = defaultdict(int)
        self.latest_time = 0 
        self.best = SortedList()


    def update(self, timestamp: int, price: int) -> None:
        self.latest_time = max(self.latest_time,timestamp)
        old_price = self.mapper[timestamp]
        self.mapper[timestamp] = price  
        self.best.add(price)
        if old_price in self.best: self.best.remove(old_price)

    def current(self) -> int:
        return self.mapper[self.latest_time]
        
    def maximum(self) -> int:
        return self.best[-1]

    def minimum(self) -> int:
        return self.best[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
        
