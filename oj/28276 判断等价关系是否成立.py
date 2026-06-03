n = int(input())
Parent = [i for i in range(26)]
def find(i):
    if (Parent[i] == i):
        return i
    else:
        result = find(Parent[i])
        Parent[i] = result
        return result
def union(i,j):
    i1 = find(i)
    j1 = find(j)
    if i1 == j1:
        return 
    Parent[i1] = j1
verdict = True
equal = []
inequal = []
for _ in range(n):
    mystr = input()
    i = ord(mystr[0])-97
    j = ord(mystr[-1])-97
    judge = mystr[1:-1]
    if judge == "==":
        equal.append((i,j))
    else:
        inequal.append((i,j))
for i,j in equal:
    union(i,j)
for i,j in inequal:
    if find(i) == find(j):
        verdict = False
print(verdict)