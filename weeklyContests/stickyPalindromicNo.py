class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(2,n-1):
            
            converted=self.converted_number(n,i)
            if(converted != str(converted)[::-1]):
                return False
    
    def converted_number(self,n,b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
        