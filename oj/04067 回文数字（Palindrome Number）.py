import sys
data = iter(sys.stdin.read().split())
while True:
    try:
        a = next(data)
        if a == a[::-1]:
            print("YES")
        else:
            print("NO")
    except StopIteration:
        break