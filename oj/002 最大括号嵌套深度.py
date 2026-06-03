s = input().strip()
stack = []
max_depth = 0
current_depth = 0
# 括号匹配映射
match = {')': '(', ']': '[', '}': '{'}

for c in s:
    if c in '([{':
        stack.append(c)
        current_depth += 1
        if current_depth > max_depth:
            max_depth = current_depth
    elif c in ')]}':
        # 栈空或不匹配
        if not stack or stack.pop() != match[c]:
            print("ERROR")
            exit()
        current_depth -= 1

# 栈不为空，有未闭合左括号
if stack:
    print("ERROR")
else:
    print(max_depth if max_depth >= 2 else 0)