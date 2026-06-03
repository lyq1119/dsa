class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if len(s) == 1:
            return True
        if s[-1] == "1":
            return False
        n = len(s)
        status = [1] * n
        for i in range(n-2,-1,-1):
            if s[i] == "1":
                status[i] = status[i+1]
                continue
            if i + minJump >= n:
                status[i] = status[i+1]
                continue
            if i + maxJump >= n-1:
                status[i] = status[i+1] + 1
                continue
            if status[i+minJump]-status[i+maxJump+1]:
                status[i] = status[i+1] + 1
            else:
                status[i] = status[i+1]
        return status[0] != status[1]