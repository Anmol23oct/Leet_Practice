class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        tasks = [1,2,1,2,3,1], space = 3
        """
        d={}
        day=0
        for ele in tasks:
            if ele not in d:
                day=day+1
                d[ele]=day
                
            else:
                req=d[ele]+space
                if day>=req:
                    day+=1
                    d[ele]=day
                    
                else:
                    br=req-day+1
                    day=day+br
                    d[ele]=day
        return day