n = int(input())
stack = []
i = 1
count = 0
for _ in range(2*n):
    s = input()
    if s == "remove":
        if stack[-1] != i:
            stack.sort(reverse=True)
            count += 1
        i += 1
        stack.pop()
        continue
    a = int(s.split()[1])
    stack.append(a)
print(count)