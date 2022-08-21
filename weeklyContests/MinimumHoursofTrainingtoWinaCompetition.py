class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        temp=0
        needener=0
        needexp=initialExperience
        temp2=0
        for ele in energy:
            temp+=ele
        temp+=1
        if initialEnergy<temp:
            needener=temp - initialEnergy
        
        for ele in experience:
            
            if needexp>ele:
                needexp+=ele
            else:
                diff=ele - needexp
                temp2=temp2+diff+1
                needexp= needexp+diff+1+ele
        print("temp2",temp2)
        print("needener",needener)
        return temp2+needener
                
            
            
        