class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:   
        arr.sort()
        result = []
        k = float("inf")
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < k:
                result = [[arr[i],arr[i+1]]]
                k = arr[i+1]-arr[i]
            elif arr[i+1]-arr[i] == k:
                result.append([arr[i],arr[i+1]]) 
        return result