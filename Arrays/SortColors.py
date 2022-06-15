class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        pivot=1
        s,mid=0,0
        e=len(nums)-1
        while mid<=e:
            
            if nums[mid]<pivot:
                self.swap(nums,s,mid)
                s=s+1
                mid=mid+1
            elif nums[mid]>pivot:
                self.swap(nums,e,mid)
                e=e-1
            else:
                mid=mid+1
    
    
    def swap(self,nums,i,j):
        
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        
        
        
        
#         if len(nums)>0:
#             pivot=nums[0]
#         d={}
#         for ele in nums:
#             d[ele]=d.get(ele,0)+1
            
#         final=[]
#         for ele in d:
            
#             if ele == 0:
#                 for i in range(d[ele]):
#                     final.append(ele)
#             elif ele==1:
#                 for i in range(d[ele]):
#                     final.append(ele)
#             else:
#                 for i in range(d[ele]):
#                     final.append(ele)
                
#         nums=final
        #return final