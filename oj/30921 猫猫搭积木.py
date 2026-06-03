import sys
def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    s = int(next(it))
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    members = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        members[i].append(i)

    pile_count = n
    out = []

    def find(i):
        if (parent[i] == i):
            return i
        else:
            result = find(parent[i])
            parent[i] = result
            return result

    for _ in range(q):
        x = int(next(it))
        y = int(next(it))
        rx = find(x)
        ry = find(y)

        if rx != ry:
            if len(members[rx]) < len(members[ry]):
                rx, ry = ry, rx
            parent[ry] = rx
            members[rx].extend(members[ry])
            members[ry].clear()
            size[rx] += size[ry]
            pile_count -= 1
            if size[rx] >= s:
                collapsed = members[rx]
                pile_count += size[rx] - 1
                for block in collapsed:
                    parent[block] = block
                    size[block] = 1
                    members[block] = [block]
                collapsed.clear()

        out.append(str(pile_count))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
