from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        newobstacles = set()
        for a,b in obstacles:
            newobstacles.add((a,b))
        x,y = 0,0
        # state:0(1,0),1(0,1),2(-1,0),3(0,-1) 左转+1，右转-1
        def move(state,units,x,y):
            if state == 0:
                for i in range(1,units+1):
                    if (x+i,y) in newobstacles:
                        i -= 1
                        break
                return x+i,y
            if state == 1:
                for i in range(1,units+1):
                    if (x,y+i) in newobstacles:
                        i -= 1
                        break
                return x,y+i
            if state == 2:
                for i in range(1,units+1):
                    if (x-i,y) in newobstacles:
                        i -= 1
                        break
                return x-i,y
            if state == 3:
                for i in range(1,units+1):
                    if (x,y-i) in newobstacles:
                        i -= 1
                        break
                return x,y-i
        maxlength = 0
        state = 1
        for num in commands:
            if num == -1:
                state -= 1
                state %= 4
                continue
            if num == -2:
                state += 1
                state %= 4
                continue
            x,y = move(state,num,x,y)
            maxlength = max(maxlength,x**2+y**2)
        return maxlength
print(Solution().robotSim([6,-1,-1,6],[[0,0]]))
