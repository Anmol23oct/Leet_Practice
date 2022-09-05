class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        n = len(nums)
        l = r = res = 0
        while r < n:
            while r < n and cur & nums[r] == 0:
                cur |= nums[r]
                r += 1
            if r == n:
                break
            res = max(res, r - l)
            while cur & nums[r] != 0:
                cur -= nums[l]
                l += 1
        return max(res, n - l)