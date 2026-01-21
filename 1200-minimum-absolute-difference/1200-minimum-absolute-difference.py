class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff=float('inf')
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            min_diff=min(min_diff,diff)
            result=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==min_diff:
                result.append([arr[i-1],arr[i]])
        return result

        