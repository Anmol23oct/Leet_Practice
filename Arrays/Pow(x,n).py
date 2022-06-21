class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def mains(x,n):
            if x==0: return 0
            if n==0: return 1
            
            final=mains(x,n//2)
            final=final*final
            return x*final if n%2 else final
        
        finals=mains(x,abs(n))
        return finals if n>=0 else 1/finals
        
#         finals=float(1)
#         t=abs(n)
#         if n>0:
#             for i in range(n,t//2,-1):
#                 finals=float(finals*x)
#         if n<0:
#             for i in range(n,t//2):
                
#                 finals=float(1/x * finals )
        
        
#         finals=float(finals*finals)
#         print(finals)
#         return float(finals*x) if n%2 else finals
        
#         if n==0:
#             return float(1)
        
#         if n<0:
            
#             return float(1/x* self.myPow(x,n+1))
#         else:
#             #print("here")
#             return float(x* self.myPow(x,n-1))
        