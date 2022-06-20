class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        d={}
        for ele in nums:
            d[ele]=d.get(ele,0)+1
        
        total=len(nums)//3
        for ele in d:
            if d[ele]>total:
                arr.append(ele)
        
        return arr