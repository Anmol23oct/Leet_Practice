class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d={}
        ans=-1
        for ele in nums:
            
            sums=self.digitSum(ele)
            #print(sums)
            if sums in d:
                #print("d[sums] b",d[sums])
                #print("ele",ele)
                if d[sums]+ele>ans:
                    #print("d[sums] in",d[sums])
                    #print("ele in",ele)
                    ans=d[sums]+ele
                    #print("answer",ans)
                
                if d[sums]<ele:
                    #print("ele b",ele)
                    d[sums]=ele
                #print("d[sums] a",d[sums])
                #print("ans",ans)
            else:
                d[sums]=ele
                
        return ans
    
    def digitSum(self,ele):
        
        sums=0
        while (ele!=0):
            sums=sums+ele%10
            ele=ele//10
            
        return sums
        
        
                
        
        