n = int(input())
directory = {}
for _ in range(n):
    mylist = input().split("\\")
    cur = directory
    i = 0
    while i < len(mylist):
        a = mylist[i]
        if a in cur:
            cur = cur[a]
            i += 1
        else:
            cur[a] = {}
            cur = cur[a]
            i += 1
def show(directory,i):
    keys = [key for key in directory]
    keys.sort()
    for key in keys:
        print((" "*i)+key)
        show(directory[key],i+1)
show(directory,0)
