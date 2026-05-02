from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        a,b = startPos
        c,d = homePos
        total = 0
        if a < c:
            for i in range(a+1,c+1):
                total += rowCosts[i]
        elif a > c:
            for i in range(c,a):
                total += rowCosts[i]
        if b < d:
            for j in range(b+1,d+1):
                total += colCosts[j]
        elif b > d:
            for j in range(d,b):
                total += colCosts[j]
        return total