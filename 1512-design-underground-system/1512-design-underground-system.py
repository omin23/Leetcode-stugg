class UndergroundSystem:

    def __init__(self):
        self.mapper = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.mapper[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        isn,ist, = self.mapper[id][0],self.mapper[id][1]
        trip = (isn,stationName)
        if trip not in self.mapper.keys(): self.mapper[trip] = [0,0]
        # updatetrip data
        time_taken  = t - ist
        avg , count = self.mapper[trip]
        new_avg = (avg*count + time_taken) / (count + 1.0)
        self.mapper[trip] = [new_avg,count + 1]

        # clean up the data
        self.mapper[id] = None


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation,endStation)
        return self.mapper[trip][0]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)