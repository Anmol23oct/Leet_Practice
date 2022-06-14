class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        flag=False
        compare=-999999999
        for i in range(len(nums)-1,-1,-1):
            
            
            
            if nums[i]<compare:
                flag=True
                pivot=i
                print("pivot",pivot)
                for i in range(len(nums)-1,i,-1):
                    
                    if nums[i] > nums[pivot]:
                        
                        t=nums[i]
                        nums[i] = nums[pivot]
                        nums[pivot] = t
                        break
                
                nums[pivot+1:] = sorted(nums[pivot+1:])
                
                
                
                
                return nums
                
                # temp=nums[i]
                # nums[i]=nums[i+1]
                # nums[i+1]=temp
                # return nums
            
            else:
                compare=nums[i]
                
        #print(flag)
        if not flag:
            #print("here")
            return nums.sort()
        
        