class Solution:
    def canReach(self, arr, start: int) -> bool:
        if arr[start] == 0:
            return True
        from collections import deque
        q = deque()
        q.append(start)
        visited = [False]*len(arr)
        visited[start] = True
        while q:
            t = q.popleft()
            if t+arr[t] < len(arr) and not visited[t+arr[t]]:
                q.append(t+arr[t])
                visited[t + arr[t]] = True
            if t-arr[t] >= 0 and not visited[t-arr[t]]:
                q.append(t-arr[t])
                visited[t-arr[t]] = True
        verdict = False
        for s in range(len(arr)):
            if arr[s] == 0:
                verdict = verdict or visited[s]
        return verdict