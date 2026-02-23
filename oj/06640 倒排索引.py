from collections import defaultdict
N = int(input())
mydict = defaultdict(set)
for i in range(N):
    i = i + 1
    mylist = input().split()
    mylist = mylist[1:]
    for word in mylist:
        mydict[word].add(i)
for _ in range(int(input())):
    mylist = list(mydict[input()])
    mylist.sort()
    if mylist:
        print(*mylist)
    else:
        print("NOT FOUND")