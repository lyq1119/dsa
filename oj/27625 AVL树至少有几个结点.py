from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return dfs(n-1) + dfs(n-2) + 1
print(dfs(int(input())))