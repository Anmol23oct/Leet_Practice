class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        n=len(matrix)
        m=-1
        if n>0:
            m=len(matrix[0])
        flag=False
        inside=False
        for i in range(n):
            
            if matrix[i][0]<=target and matrix[i][m-1]>=target:
                inside= True
                for i in range(n):
                    for j in range(m):
                        
                        if matrix[i][j]==target:
                            flag=True
                            break
            
            if inside:
                break
            
        
        return flag
                        
        