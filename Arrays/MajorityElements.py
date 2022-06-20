import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lens=len(nums)
        
        if lens==0:
            return
        
        d={}
        for ele in nums:
            d[ele]=d.get(ele,0)+1
        
        total=lens//2
        # print(total)
        # c= math.ceil(total)
        # print(c)
        for ele in d:
            print(ele)
            if d[ele]>total:
                return ele
        
        
            
        
            
        