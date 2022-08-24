class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights: return[]
        row=len(heights)
        col=len(heights[0])
        a=[]
        p=[]
        va=set()
        vp=set()
        for r in range(row):
            a.append((r,col-1))
            p.append((r,0))
        
        for c in range(col):
            a.append((row-1,c))
            p.append((0,c))
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,visited):
            
            visited.add((i,j))
            
            for di,dj in direction:
                
                newi=i+di
                newj=j+dj
                
                if 0<=newi<row and 0<=newj<col and heights[newi][newj]>=heights[i][j] and (newi,newj) not in visited:
                    dfs(newi,newj,visited)
                
        for r,c in a:
            dfs(r,c,va)
        for r,c in p:
            dfs(r,c,vp)
        
        return vp&va
                
            
        
        