class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(grid)
        maxlocal=[[-1 for i in range(m-2)] for i in range(m-2)]
        for i in range(len(maxlocal)):
            for j in range(len(maxlocal)):
                k,l=i+1,j+1
                maxlocal[i][j]=self.FindMax(k,l,grid)
        return maxlocal
    
    def FindMax(self,i,j,grid):
        
        maxs=-1
        search=[(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j), (i,j+1), (i+1, j-1), (i+1,j), (i+1,j+1)]
        
        #print("here",i,j)
        for k,l in search:
            maxs=max(maxs,grid[k][l])
            
        
        return maxs
            
        