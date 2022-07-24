class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for ele in s:
            d[ele]=d.get(ele,0)+1
            if d[ele]==2:
                return ele
        
        
        