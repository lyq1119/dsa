import sys
data = sys.stdin.read().split()
wenjian = []
dijige = 1
cur = 0
mulu = 0
flag = True
def dfs(i,j,mulu):
    curmulu = mulu
    wenjian = []
    cur = i
    while cur <= j:
        if data[cur][0] == "f":
            wenjian.append(data[cur])
            cur += 1
        if data[cur][0] == "d":
            print("|     "*(mulu+1)+data[cur])
            cur1 = cur
            curmulu += 1
            cur += 1
            while True:
                if data[cur] == "]":
                    curmulu -= 1
                elif data[cur][0] == "d":
                    curmulu += 1
                if curmulu == mulu and data[cur] == "]":
                    break
                cur += 1
            dfs(cur1+1,cur-1,mulu+1)
            cur += 1
    for item in sorted(wenjian):
        print("|     "*mulu+item)
while True:
    a = data[cur]
    if a == "#":
        break
    if flag:
        print(f"DATA SET {dijige}:")
        print("ROOT")
        flag = False 
    if a == "*":
        dijige += 1
        if data[cur+1] != "#":
            print("")
        flag = True
        wenjian = []
        mulu = 0
        cur += 1
    else:
        m = 0
        for t in range(cur,len(data)):
            if data[t] == "*":
                m = t-1
                break
        dfs(cur,m,0)
        cur = m+1