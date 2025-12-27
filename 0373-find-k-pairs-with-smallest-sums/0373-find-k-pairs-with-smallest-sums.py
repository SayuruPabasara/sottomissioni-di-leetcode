import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 and not nums2 and k<=0:
            return []
        heap=[]
        results=[]
        for i in range(min(k,len(nums1))):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        while heap and len(results)<k:
            _,i,j=heapq.heappop(heap) 
            results.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return results


            
        