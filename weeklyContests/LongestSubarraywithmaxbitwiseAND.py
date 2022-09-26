class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we have taken AND in such a way that adjacent numbers are same then it has max And value otherwise we've to reset it to max number, here we're assigning max value to m and checking if multiple adjacent m's are there or not.
        m=max(nums)
        best=0
        current=0
        for x in nums:
            if x==m:
                current+=1
            else:
                current=0
            
            best=max(best,current)
        return best
#         sums=nums[0]
#         k=1
#         finalk=1