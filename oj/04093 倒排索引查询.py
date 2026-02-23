N = int(input())
from collections import defaultdict
mydict = defaultdict(set)
for i in range(N):
    mylist = list(map(int,input().split()))
    mylist = mylist[1:]
    for num in mylist:
        mydict[num].add(i)
for _ in range(int(input())):
    mylist = list(map(int,input().split()))
    setfor1 = set()
    setfor0 = set()
    for index,num in enumerate(mylist):
        if num == 1:
            setfor1.add(index)
        elif num == -1:
            setfor0.add(index)
    wendang = {key for key in mydict}
    result = []
    for i in wendang:
        myset = mydict[i]
        flag = True
        for num in setfor0:
            if num in myset:
                flag = False
                break
        if not flag:
            continue
        for num in setfor1:
            if num not in myset:
                flag = False
                break
        if not flag:
            continue
        result.append(i)
    if result:
        print(*result)
    else:
        print("NOT FOUND")