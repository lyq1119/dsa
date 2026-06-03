while True:
    n,k = map(int,input().split())
    if n == -1 and k == -1:
        break
    matrix = []
    for _ in range(n):
        mylist = list(input())
        matrix.append(mylist)
    count = 0
    myset = set()
    def backtrack(i,s): # 第i行已经填了s个
        global count
        if s == k:
            count += 1
            return
        if i == n:
            return
        backtrack(i+1,s)
        for t in range(n):
            if t in myset:
                continue
            if matrix[i][t] == ".":
                continue
            myset.add(t)
            backtrack(i+1,s+1)
            myset.discard(t)
    backtrack(0,0)
    print(count)
