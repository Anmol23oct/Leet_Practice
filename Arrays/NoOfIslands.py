 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr, nc, num_islands = len(grid), len(grid[0]), 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(r, c):
            queue = deque([])
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                if 0 <= r < nr and 0 <= c < nc and grid[r][c] == "1":
                    grid[r][c] = "0"
                    for d_r, d_c in directions:
                        queue.append((r + d_r, c + d_c))
                
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)
        
        return num_islands
#         def bfs(i,j):
#             queue = collections.deque()
            
#             queue.appendleft((i,j))
#             visi
#             #queue.
#             #print(queue.c)
#             while queue:
#                 #print(queue.pop())
#                 ele=queue.popleft()
#                 #print(ele)
#                 x=ele[0]
#                 y=ele[1]
                
#                 grid[x][y]="2"
                
#                 if (x-1)>=0 and grid[x-1][y]=="1":
#                     #print("here",i,j)
#                     queue.appendleft((x-1,y))
                
#                 if (x+1)<row and grid[x+1][y]=="1":
#                     queue.appendleft((x+1,y))
                    
#                 if (y+1)<col and grid[x][y+1]=="1":
#                     queue.appendleft((x,y+1))
                
#                 if (y-1)>=0 and grid[x][y-1]=="1":
#                     queue.appendleft((x,y-1))
            
        
        
        
#         row=len(grid)
#         col=len(grid[0])
#         count=0
#         visit=set()
#         for i in range(row):
#             for j in range(col):
                
#                 if grid[i][j]=="1" and (i,j) not in visit:
#                     #print("here")
#                     bfs(i,j)
#                     count=count+1
#         return count
        
#         for i in range(row):
#             for j in range(col):
#                 flag=0
#                 if (i-1)>=0 and grid[i-1][j]=="2":
#                     #print("here",i,j)
#                     flag=1
                
#                 elif (i+1)<row and grid[i+1][j]=="2":
#                     flag=1
                    
#                 elif (j+1)<col and grid[i][j+1]=="2":
#                     flag=1
                
#                 elif (j-1)>=0 and grid[i][j-1]=="2":
#                     #print("here",i,j)
#                     flag=1
                
                
#                 if grid[i][j]=="1":
#                     #print("here2",i,j)
#                     grid[i][j]="2"
#                     #print("here3",grid[i][j])
                    
                                
#                 if flag==0 and grid[i][j]!="0":
#                     print("grid",grid[i][j])
#                     print("i,j",i,j)
#                     count=count+1
                    
                    
                    
                    
        return count