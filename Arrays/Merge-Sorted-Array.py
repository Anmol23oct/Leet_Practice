class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        l1=m-1
        l2=n-1
        fi=m+n-1
        
        while( l1>=0 and l2>=0):
            #print("fi",fi)
            if nums1[l1]>=nums2[l2]:
                #print(nums1[l1])
                nums1[fi]=nums1[l1]
                l1=l1-1
                
            
            elif nums1[l1]<nums2[l2]:
                nums1[fi]=nums2[l2]
                l2=l2-1
                
            fi=fi-1
        #print("l1,l2",l1,l2)
        #print("fi again",fi)
        while(l1>=0):
            
            nums1[fi]=nums1[l1]
            l1=l1-1
            fi=fi-1
            
        while(l2>=0):
            #print("l2,fi",l2,fi)
            nums1[fi]=nums2[l2]
            l2=l2-1
            fi=fi-1
                
                
        
#         replace=m
#         a1=0
#         a2=0
        
#         if len(nums2)==0:
#             return nums1
        
#         if len(nums1)==0:
#             return nums2
        
        
#         while(a1<m):
#             #print("a1=",a1)
#             if nums1[a1]<=nums2[a2]:
                
#                 a1=a1+1
                
#             else:
                
#                 temp=nums1[a1]
#                 nums1[a1]=nums2[a2]
#                 nums2[a2]=temp
#         #print(nums1)       
#         while(a1<m+n):
            
#             temp=nums1[a1]
#             nums1[a1]=nums2[a2]
#             nums2[a2]=temp
#             a1=a1+1
#             a2=a2+1

            
                