class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        def mintime(i1,j1,i2,j2):
            return max(abs(i2-i1),abs(j2-j1))
        total = 0
        for i in range(len(points)-1):
            total += mintime(points[i][0],points[i][1],points[i+1][0],points[i+1][1])
        return total