import heapq
class MedianFinder:
    def __init__(self):
        self.zuoban = []
        self.youban = []
        self.zuobanzuida = None
        self.youbanzuixiao = None
        self.middle = None
    def addNum(self, num: int) -> None:
        if self.middle != 0 and not self.middle:
            if not self.zuoban:
                self.middle = num
                return
            if num <= self.zuobanzuida:
                heapq.heappush(self.zuoban,-num)
                self.middle = -heapq.heappop(self.zuoban)
                self.zuobanzuida = -heapq.heappop(self.zuoban)
                heapq.heappush(self.zuoban,-self.zuobanzuida)
            elif num >= self.youbanzuixiao:
                heapq.heappush(self.youban,num)
                self.middle = heapq.heappop(self.youban)
                self.youbanzuixiao = heapq.heappop(self.youban)
                heapq.heappush(self.youban,self.youbanzuixiao)
            else:
                self.middle = num
        else:
            if num <= self.middle:
                heapq.heappush(self.youban,self.middle)
                self.youbanzuixiao = self.middle
                self.middle = None
                self.zuobanzuida = -heapq.heappushpop(self.zuoban,-num)
                heapq.heappush(self.zuoban,-self.zuobanzuida)
            else:
                heapq.heappush(self.zuoban,-self.middle)
                self.zuobanzuida = self.middle
                self.middle = None
                self.youbanzuixiao = heapq.heappushpop(self.youban,num)
                heapq.heappush(self.youban,self.youbanzuixiao)
    def findMedian(self) -> float:
        if self.middle or self.middle == 0:
            return self.middle
        else:
            return (self.youbanzuixiao+self.zuobanzuida)/2
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.zuoban,obj.youban,obj.zuobanzuida,obj.youbanzuixiao)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())