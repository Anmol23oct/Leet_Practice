class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet=set(nums)
        
        lon=0
        
        for n in nums:
            if (n-1) not in numSet:
                length=0
                while(n+length) in numSet:
                    length+=1
                lon=max(length,lon)
            
        return lon
        
#         d={}
#         for ele in nums:
#             d[ele]=0
#         visited=set()
#         for ele in :
            
#             visited.add(ele)
#             count=1
#             print("v",visited)
            
#             while((ele-1 in d) and (ele-1 not in visited) ):
#                 print("here")
#                 visited.add(ele-1)
#                 count=count+1
#                 ele=ele-1
            
#             while((ele+1 in d) and (ele+1 not in visited) ):
#                 print("here")
#                 visited.add(ele-1)
#                 count=count+1
#                 ele=ele-1
#             d[ele]=count
            
#         final=-1
#         print(d)
#         for ele in d:
#             if d[ele]>final:
#                 final=d[ele]
#         return final
            
                
                
            
            
                
            
            
#         print(d)
        