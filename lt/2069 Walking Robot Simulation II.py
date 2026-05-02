from typing import List
class Robot:
    def __init__(self, width: int, height: int):
        self.width = width #长度是第一个分量
        self.height = height
        self.pos = (0,0)
        self.begin = False
    def step(self, num: int) -> None:
        x,y = self.pos
        mydict = {"East":0,"North":1,"West":2,"South":3}
        state = mydict[self.getDir()]
        num %= (self.width+self.height-2)*2
        while num > 0:
            if state == 0:
                if x+num >= self.width:
                    num = x+num-self.width+1
                    x,y = self.width-1,y
                    state = (state+1)%4
                else:
                    x,y = x+num,y
                    num = 0
                continue
            elif state == 1:
                if y+num >= self.height:
                    num = y+num-self.height+1
                    x,y = x,self.height-1
                    state = (state+1)%4
                    
                else:
                    x,y = x,y+num
                    num = 0
                continue
            elif state == 2:
                if x-num < 0:
                    num = num-x
                    x,y = 0,y
                    state = (state+1)%4
                    
                else:
                    x,y = x-num,y
                    num = 0
                continue
            else:
                if y-num < 0:
                    num = num-y
                    x,y = x,0
                    state = (state+1)%4
                    
                else:
                    x,y = x,y-num
                    num = 0
                continue
        self.pos = (x,y)
        self.begin = True

    def getPos(self) -> List[int]:
        return [self.pos[0],self.pos[1]]

    def getDir(self) -> str:
        x,y = self.pos
        if not self.begin:
            return "East"
        if x > 0 and x <= self.width-1 and y == 0:
            return "East"
        if x >= 0 and x < self.width-1 and y == self.height-1:
            return "West"
        if x == self.width-1 and y > 0 and y <= self.height-1:
            return "North"
        if x == 0 and y >= 0 and y < self.height-1:
            return "South"

obj = Robot(6, 3)
obj.step(4)
print(obj.getPos())
print(obj.getDir())
obj.step(2)
print(obj.getPos())
print(obj.getDir())
obj.step(1)
print(obj.getPos())
print(obj.getDir())
obj.step(4)
print(obj.getPos())
print(obj.getDir())