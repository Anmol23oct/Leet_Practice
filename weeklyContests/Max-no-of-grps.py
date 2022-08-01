class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        grades.sort()
        grp=1
        grplen=1
        total=1
        #sums=grades[0]
        
        while True:
            
            grplen+=1
            total+=grplen
            if total<=len(grades):
                grp+=1
            else:
                break
        
        return grp
            
            
            
            
        