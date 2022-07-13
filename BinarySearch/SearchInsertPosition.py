class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        last= len(nums)-1
        mid=0
        
        while start<=last:
            mid=(start+last)//2
            #print("mid",mid)
            #print("start",start)
            #print("last",last)
            if nums[mid]>target:
                last=mid-1
            elif nums[mid]==target:
                return mid
            else:
                start=mid+1
        return start
                