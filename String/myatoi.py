class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if len(s)==0:
            return 0
        flag=False
        pos_limit = 2147483647
        neg_limit = -2147483648
        neg=False
        
        if s[0]=="-":
            neg=True
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]
        
        val=0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            
            val=val*10+int(s[i])
        
        
        print(val)
        if neg:
            val= -1*val
        if neg and int(val)<neg_limit:
            return neg_limit
        elif int(val)>pos_limit:
            return pos_limit
        else:
        
        
            return val
        
#         while i<len(s):
            
#             if s[i]=='+' or s[i]=='-' or s[i].isdigit():
#                 if s[i]=="-":
#                     neg=True
#                     temp=list(s)
#                     temp[:i]="-"
#                     s="".join(temp)
                
#                 flag=True
#                 i=i+1
#             elif s[i]==" ":
#                 temp=list(s)
#                 temp[i]=""
#                 s="".join(temp)
#                 flag=True
#             else:
#                 temp=list(s)
#                 temp[i:]=""
#                 s="".join(temp)
#                 break
            
#             if flag is False:
#                 return 0
#         if len(s)==0:
#             return 0
        
#         elif neg and int(s)<neg_limit:
#             return neg_limit
#         elif int(s)>pos_limit:
#             return pos_limit
#         else:
#             return int(s)
                
                
        