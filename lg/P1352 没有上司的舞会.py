import sys
from collections import deque
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1

    val = [0] * (N + 1)  # 1~N
    for i in range(1, N+1):
        val[i] = int(data[idx])
        idx += 1

    # 建树
    children = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)

    for _ in range(N-1):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        children[b].append(a)
        in_degree[a] += 1

    # 找根
    root = -1
    for i in range(1, N+1):
        if in_degree[i] == 0:
            root = i
            break

    # DP
    dp0 = [0] * (N + 1)  # 不选
    dp1 = [0] * (N + 1)  # 选

    # 后序遍历（迭代版，不爆栈）
    stack = [(root, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            dp1[node] = val[node]
            dp0[node] = 0
            for ch in children[node]:
                dp1[node] += dp0[ch]
                dp0[node] += max(dp0[ch], dp1[ch])
            # 不能为负
            dp1[node] = max(dp1[node], 0)
            dp0[node] = max(dp0[node], 0)
        else:
            stack.append((node, True))
            # 逆序入栈保证顺序
            for ch in reversed(children[node]):
                stack.append((ch, False))

    print(max(dp0[root], dp1[root]))

if __name__ == "__main__":
    main()