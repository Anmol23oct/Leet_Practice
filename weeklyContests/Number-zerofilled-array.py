class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        count=0
        start=-1
        end=-1
        
        for i in range(len(nums)):
            
            if nums[i]==0:
                
                end=i
                
                count=count+(end-start)
                # d[(end-start)]=d.get((end-start),0)+1
                # temp=start+1
                # while (end-temp)>0:
                #     d[(end-temp)]=d.get((end-temp),0)+1
                #     temp=temp+1
                    
            
            else:
                start=i
                end=i
        # print(d)
        # for ele in d:
        #     count=count+d[ele]

        return count
                
                
                
        