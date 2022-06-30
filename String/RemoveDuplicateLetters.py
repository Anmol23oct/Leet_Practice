class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        d1={}# for indexes
        d2={}# for true and false
        
        for i,ele in enumerate(s):
            d1[str(ele)]=i
        stack.append(str(s[0]))   
        d2[str(s[0])]=True
        for i in range(1,len(s)):
            
            if str(s[i]) not in d2:
                
                while len(stack)>0 and (ord(str(s[i]))<ord(stack[-1])) and d1[stack[-1]]>i:
                    e=stack.pop()
                    d2.pop(e)
                
            
                
                stack.append(str(s[i]))
                d2[str(s[i])]=True
        
        final=""
        for ele in stack:
            final=final+ele
        return final
#         s1=""
#         for ele in s:
#             if ele not in s1:
#                 if len(s1)>0 and ord(ele)<ord(s1[0]):
#                     s1=""
                
#                 s1=s1+ele
        
#         return s1
                
                    
                
        