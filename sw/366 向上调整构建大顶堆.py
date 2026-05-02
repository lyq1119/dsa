import sys
data = iter(sys.stdin.read().split())
n = int(next(data))
heap = [int(next(data)) for _ in range(n)]
def tiaozheng(i):
    '''向上调整heap[i]'''
    if i == 0:
        return 
    c_val = heap[i]
    p_val = heap[(i-1)//2]
    if c_val > p_val:
        heap[i],heap[(i-1)//2] = p_val,c_val
        tiaozheng((i-1)//2)
for i in range(n):
    tiaozheng(i)
print(*heap)