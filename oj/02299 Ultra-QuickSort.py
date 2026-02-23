import sys
input = sys.stdin.read().split()
data = iter(input)
while True:
    n = int(next(data))
    if n == 0:
        break
    count = [0]
    mylist = [int(next(data)) for _ in range(n)]
    def mergesort(i,j):
        if i == j:
            return [mylist[i]]
        mid = (i+j)//2
        list1 = mergesort(i,mid)
        list2 = mergesort(mid+1,j)
        t,s = 0,0
        cur = i
        while cur <= j:
            if t < len(list1) and s < len(list2):
                if list1[t] > list2[s]:
                    mylist[cur] = (list2[s])
                    s += 1
                    count[0] += (s+len(list1)-(cur-i+1))
                    cur += 1
                else:
                    mylist[cur] = (list1[t])
                    t += 1
                    cur += 1
            elif t < len(list1):
                mylist[cur] = (list1[t])
                t += 1
                cur += 1
            elif s < len(list2):
                mylist[cur] = (list2[s])
                s += 1
                cur += 1
            else:
                break
        return mylist[i:j+1]
    mergesort(0,n-1)
    print(count[0])