class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=""
        finals= self.recstr(1,n,s)
        return finals
    
    def recstr(self,x,n,s):
        
        if n==1:
            s=s+"1"
            return s
        
        if x==1:
            s=s+"1"
            
        if x==n-1:
            return self.op(s)
        
        s=self.op(s)
        return self.recstr(x+1,n,s)
        
        
        
    def op(self,s):
        
        d=""
        c=1
        for i in range(1,len(s)):
            
            
            if s[i-1]==s[i]:
                c=c+1
                
            else:
                d=d+str(c)+s[i-1]
                c=1
        
        #print(s)
        if len(s)>0:
            
            d=d+str(c)+s[len(s)-1]
        
        return d
        
                