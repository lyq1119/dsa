import random
class RandomizedSet:
    def __init__(self):
        self.suoyin = {}
        self.zhi = {}
    def insert(self, val: int) -> bool:
        if val in self.zhi:
            return False
        self.zhi[val] = len(self.suoyin)+1
        self.suoyin[len(self.zhi)] = val
        return True
    def remove(self, val: int) -> bool:
        if val in self.zhi:
            a = self.zhi[val]
            val1 = self.suoyin[len(self.zhi)]
            self.zhi[val1] = a
            self.suoyin[a] = val1
            del self.zhi[val]
            del self.suoyin[len(self.suoyin)]
            return True  
        return False
    def getRandom(self) -> int:
        t = random.randint(1,len(self.suoyin))
        return self.suoyin[t]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()