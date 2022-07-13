# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        mid=0
        last=n
        
        while start<=last:
            mid=(start+last)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                last=mid-1
            
            else:

                if isBadVersion(mid+1):
                    return mid+1 
                start=mid+1
        