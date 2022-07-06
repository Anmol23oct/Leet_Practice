class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        temp=[i for i in range(n)]
        #print("before",temp)
        visited=set()
        for u in edges:
            p=u[0]
            c=u[1]
            visited.add(p)
            
            fp=p
            print(p)
            while temp[p]!=p:
                p=temp[p]
                fp=p
            
            fc=c
            while temp[c]!=c:
                c=temp[c]
                fc=c
            
            if temp[fp]==temp[fc]:
                return False
            
            temp[c]=fp
        #print("After",temp)   
        
        if len(edges)!=n-1:
            return False
        return True
#         visited=set()
#         d={i:[] for i in range(n)}
#         for ele in edges:
#             d[ele[0]].append(ele[1])
        
#         #print(d)
        
#         def dfs(ele,visited):
#             #print(ele)
#             if ele in visited:
                
#                 return False
            
            
#             if d[ele]==[]:
#                 return True
            
#             visited.add(ele)
            
#             for nb in d[ele]:
#                 if not dfs(nb,visited): return False
            
#             visited.remove(ele)
#             d[ele]=[]
            
#             return True
                
            
                
            
        
#         for ele in d:
#             #visited.add(ele)
#             if not dfs(ele,visited): return False
        
#         #print(d)
        
#         return True
        
        
        
        
        