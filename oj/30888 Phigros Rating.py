n,b = map(int,input().split())
mylist = []
for _ in range(n):
    d,a = map(int,input().split())
    if a == 100:
        mylist.append(d)
    elif a >= 95:
        mylist.append(d*(0.5+(a/200)))
    elif a >= 70:
        mylist.append(d*((a/150)-1/6))
    else:
        mylist.append(0)
mylist.sort(reverse=True)
if n <= b:
    print(f"{sum(mylist)/n:.6f}")
else:
    print(f"{sum(mylist[:b])/b:.6f}")
