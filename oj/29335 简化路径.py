s = input().split("/")
n = len(s)
stack = []
for i in range(n):
    t = s[i]
    if t == "":
        continue
    if t == ".":
        continue
    if t == "..":
        if stack:
            stack.pop()
        continue
    stack.append(t)
print("/"+"/".join(stack))