class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        sets=set(s)
        d={}
        for ele in sets:
            d[str(ele)]=[]
        for i in range(len(s)):
            
            d[str(s[i])].append(i)
        
        count=0
        for word in words:
            c=-1
            isValid=True
            for letter in word:
                if letter in d:
                    prev=c
                    for ele in d[letter]:
                        if ele>c:
                            c=ele
                            break
                    if c==prev:
                        isValid=False
                        break
                else:
                    isValid=False
                    break
            if isValid:
                count=count+1
        
        return count
        
        #print(d)
#         subseq=self.GetAllSubsequence(s)
#         #print(subseq)
#         s=set(subseq)
#         count=0
#         for ele in words:
#             if ele in s:
#                 count+=1
        
#         return count
        
        
#     def GetAllSubsequence(self,s):
        
#         if len(s)==0:
#             output=[]
#             output.append(str(""))
#             return output
        
#         smallstring=self.GetAllSubsequence(s[1:])
#         output=[]
#         for ele in smallstring:
#             output.append(str(ele))
            
#         for ele in smallstring:
#             subszero=s[0]+ele
#             output.append(str(subszero))
        
#         return output
        