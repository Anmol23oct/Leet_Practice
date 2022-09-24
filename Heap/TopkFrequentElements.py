import heapq as hq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Bucket Sort
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
            
        # - value because we need max heap elements.
        heap = [(-values,key) for key,values in d.items()]
        
        heapify(heap)
        ans = []
        for i in range(k):
            temp = heappop(heap)
            ans.append(temp[1])
        
        
        return ans
        