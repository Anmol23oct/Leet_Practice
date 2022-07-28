class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(nums)-1
        ans=[]
        flag=False
        while(end>=start):
            mid=(start+end)//2
            if target>nums[mid]:
                start=mid+1
            elif target<nums[mid]:
                end=mid-1
            else:
                flag=True
                break
        
        if flag:
            high=mid
            low=mid
            while high+1<len(nums) and nums[high+1]==target:
                high=high+1
                # ans.append(mid)
                # ans.append(mid+1)
            while low-1>=0 and nums[low-1]==target:
                low=low-1
            
            ans.append(low)
            ans.append(high)
                
        
        if len(ans)==0:
            return [-1,-1]
        return ans
                
                
        