import sys
from collections import defaultdict,deque
data = iter(sys.stdin.read().split())
n = int(next(data))
buckets = defaultdict(list)
linjiebiao = defaultdict(set)
for _ in range(n):
    word = next(data)
    for i in range(4):
        bucket = word[:i]+"_"+word[(i+1):]
        for neighbor in buckets[bucket]:
            linjiebiao[word].add(neighbor)
            linjiebiao[neighbor].add(word)
        buckets[bucket].append(word)
begin,end = next(data),next(data)
queue = deque([begin])
visited = {begin}
prev = {begin:None}
flag = False
while queue:
    word = queue.popleft()
    if word == end:
        flag = True
        cur = end
        result = []
        while prev[cur]:
            result.append(cur)
            cur = prev[cur]
        result.append(begin)
        print(*list(reversed(result)))
        break
    for neighbor in linjiebiao[word]:
        if neighbor not in visited:
            queue.append(neighbor)
            prev[neighbor] = word
            visited.add(neighbor)
if not flag:
    print("NO")