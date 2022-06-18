class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums)==0:
            return
        maxs=-999999
        for k in range(len(nums)-2):
            maxs=max(nums[k],maxs)
            if maxs>nums[k+2]:
                return False
            
        
        
        return True
            
                
        