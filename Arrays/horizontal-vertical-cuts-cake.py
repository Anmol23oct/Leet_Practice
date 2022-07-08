class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts=[0]+horizontalCuts+[h]
        verticalCuts=[0]+verticalCuts+[w]
        
        max_h,max_w=0,0
        for i in range(1,len(horizontalCuts)):
            max_h=max(max_h,abs(horizontalCuts[i-1]-horizontalCuts[i]))
            
        for i in range(1,len(verticalCuts)):
            max_w=max(max_w,abs(verticalCuts[i-1]-verticalCuts[i]))
            
        return (max_h*max_w)%1000000007
        
#         maxs=h*w
#         horizontalCuts.sort()
#         verticalCuts.sort()
#         prevh=0
#         for ele in horizontalCuts:
#             minus=w*(ele-prevh)
#             maxs=maxs-minus
#             maxs=max(minus,maxs)
#             prevh=ele
        
#         cuth=maxs/w
#         #print("maxs",maxs)
#         #print("cuth",cuth)
#         prevw=0
#         for ele in verticalCuts:
#             minus=cuth*(ele-prevw)
#             maxs=maxs-minus
#             #print("maxs here",maxs)
#             #print("minus here",minus)
#             maxs=max(minus,maxs)
#             #print("maxs here2",maxs)
#             prevw=ele
        
#         return maxs %(1000000007)