class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oper=0
        s=set(nums)
        while(len(s)>1):
            mins=self.FindMin(s)
            #print(mins)
            for i in range(len(nums)):
                if nums[i]>0:
                    nums[i]=nums[i]-mins
            #print(nums)
            oper+=1 
            s=set(nums)
        if s.pop()>0:
            return oper+1
        else:
            return oper
        
        
        
        
        # oper=0
        # s=set(nums)
#         while(len(s)>1 ):
#             mins=self.FindMin(s)
#             print(mins)
#             for i in range(len(nums)):
#                 nums[i]=nums[i]-mins
#             oper+=1
            
#             s=set(nums)
        
#         return oper
    
    def FindMin(self,s):
        
        mins=9999999
        for ele in s:
            if ele< mins and ele>0:
                mins=ele
        
        return mins
            
        
        