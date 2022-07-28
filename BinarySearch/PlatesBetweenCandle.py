class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        left=[-1]*len(s)
        right=[-1]*len(s)
        prefix=[0]
        # finding left side candle
        for i in range(len(s)):
            if s[i]=="|":
                left[i]=i
            else:
                if i>0:
                    left[i]=left[i-1]
        # finding right side candle
        for i in range(len(s)-1,-1,-1):
            if s[i]=="|":
                right[i]=i
            else:
                if i<len(s)-1:
                    right[i]=right[i+1]
        #calculate prefix sum of no of plates
        for i in range(len(s)):
            if s[i]=="*":
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])
        ans=[]
        
        #calculate answer through prefix sum 
        #left side plate will be calculated with right side candle and vice versa
        for l,r in queries:
            l=right[l]
            r=left[r]
            #print("l",l)
            #print("r",r)
            if l>r or l==-1 or r==-1:
                ans.append(0)
            else:
                ans.append(prefix[r]-prefix[l])
        
        
        return ans