import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    # 线段树数组 & 懒标记
    size = 1
    while size < N:
        size <<= 1
    tree = [0] * (2 * size)
    lazy = [0] * (2 * size)

    # 向下传递懒标记
    def push_down(node, l, r):
        if lazy[node] != 0 and node < size:
            # 左孩子
            tree[2*node] += lazy[node]
            lazy[2*node] += lazy[node]
            # 右孩子
            tree[2*node+1] += lazy[node]
            lazy[2*node+1] += lazy[node]
            # 清空当前节点懒标记
            lazy[node] = 0

    # 区间加 v
    def update(a, b, v, node=1, l=1, r=None):
        if r is None:
            r = size
        if a > r or b < l:
            return
        if a <= l and r <= b:
            tree[node] += v
            lazy[node] += v
            return
        push_down(node, l, r)
        mid = (l + r) // 2
        update(a, b, v, 2*node, l, mid)
        update(a, b, v, 2*node+1, mid+1, r)
        tree[node] = max(tree[2*node], tree[2*node+1])

    # 区间查询最大值
    def query(a, b, node=1, l=1, r=None):
        if r is None:
            r = size
        if a > r or b < l:
            return -float('inf')
        if a <= l and r <= b:
            return tree[node]
        push_down(node, l, r)
        mid = (l + r) // 2
        left = query(a, b, 2*node, l, mid)
        right = query(a, b, 2*node+1, mid+1, r)
        return max(left, right)

    # 处理询问
    output = []
    for _ in range(Q):
        op = data[idx]
        idx += 1
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        if op == 'Add':
            v = int(data[idx])
            idx += 1
            update(l, r, v)
        else:
            res = query(l, r)
            output.append(str(res))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()