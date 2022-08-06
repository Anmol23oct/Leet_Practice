class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tot = n * (n - 1) // 2
        good = 0
        memo = Counter()
        for i, v in enumerate(nums):
            tar = i - v
            #print("tar",tar)
            good += memo[tar]
            #print("good",good)
            memo[tar] += 1
            #print("memo",memo[tar])
            #print()
        return tot - good
        