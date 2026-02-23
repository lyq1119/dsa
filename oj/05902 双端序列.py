class Shuangduanxulie:
    def __init__(self):
        self.seq = []
    def jindui(self,data):
        self.seq.append(data)
    def chudui(self,c):
        if c == 0:
            self.seq.pop(0)
        else:
            self.seq.pop()
    def __str__(self):
        if self.seq:
            return " ".join([str(m) for m in self.seq])
        else:
            return ("NULL")
import sys
data = iter(sys.stdin.read().split())
t = int(next(data))
for _ in range(t):
    shuangduanxulie = Shuangduanxulie()
    n = int(next(data))
    for __ in range(n):
        a = int(next(data))
        b = int(next(data))
        if a == 1:
            shuangduanxulie.jindui(b)
        else:
            shuangduanxulie.chudui(b)
    print(shuangduanxulie)