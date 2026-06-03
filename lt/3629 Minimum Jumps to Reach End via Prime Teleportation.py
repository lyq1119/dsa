from collections import defaultdict, deque
class Solution:
    def minJumps(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        MAXV = max(nums)
        # 欧拉筛 + 最小质因子
        spf = [0] * (MAXV + 1)
        primes = []
        for i in range(2, MAXV + 1):
            if spf[i] == 0:
                spf[i] = i
                primes.append(i)
            for p in primes:
                if p > spf[i] or i * p > MAXV:
                    break
                spf[i * p] = p
        # 判断质数
        def is_prime(x):
            return x >= 2 and spf[x] == x
        # 质因数分解
        def get_factors(x):
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors
        prime_to_indices = defaultdict(list)
        for i, x in enumerate(nums):
            for p in get_factors(x):
                prime_to_indices[p].append(i)
        # BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        used_prime = set()
        while q:
            i = q.popleft()
            step = dist[i] + 1
            if i == n - 1:
                return dist[i]
            # 相邻跳
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = step
                    q.append(ni)
            # teleport
            x = nums[i]
            if is_prime(x) and x not in used_prime:
                for ni in prime_to_indices[x]:
                    if dist[ni] == -1:
                        dist[ni] = step
                        q.append(ni)
                used_prime.add(x)
        return -1