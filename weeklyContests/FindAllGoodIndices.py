class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int
        """
        #take nonincreasing from left index, take nondecreasing from right index,  
        n = len(nums)
        bef = [1]*n
        after = [1]*n
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                bef[i] = bef[i-1]+1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                after[i] = after[i+1]+1
 
        res = []
        # now finally calculate according to the question
        for i in range(k, n-k):
            if bef[i-1] >= k and after[i+1] >= k:
                res.append(i)
        return res
        