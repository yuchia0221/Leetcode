from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.customers = dict()
        self.travel_time = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [stationName, t]

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, checkInTime = self.customers[id]
        self.travel_time[(startStation, endStation)][0] += (t - checkInTime)
        self.travel_time[(startStation, endStation)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, customerNum = self.travel_time[(startStation, endStation)]
        return totalTime / customerNum
