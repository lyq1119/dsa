from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def zhaozuichanglianxu(mylist):
            mymax = 1
            cur = 1
            for i in range(1,len(mylist)):
                if mylist[i] - mylist[i-1] == 1:
                    cur += 1
                else:
                    cur = 1
                mymax = max(mymax,cur)
            return mymax
        return (1+min(zhaozuichanglianxu(sorted(hBars)),zhaozuichanglianxu(sorted(vBars))))**2