import sys
input = sys.stdin.read()
data = input.split()
i = 0
while data[i] != "-1" and data[i+1] != "-1":
    n,k = int(data[i]),int(data[i+1])
    i += 2
    matrix = [list(data[i+j]) for j in range(n)]
    i += n
    count = [0]
    visited = set()
    def backtrack(hang,geshu):
        if hang >= n:
            if geshu == k:
                count[0] += 1
            return
        if geshu == k:
            count[0] += 1
            return
        row = matrix[hang]
        for i in range(n):
            if i not in visited and row[i] == "#":
                visited.add(i)
                backtrack(hang+1,geshu+1)
                visited.discard(i)
        backtrack(hang+1,geshu)
    backtrack(0,0)
    print(count[0])