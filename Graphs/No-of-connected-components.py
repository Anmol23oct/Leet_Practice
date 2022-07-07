class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        par=[i for i in range(n)]
        rank=[1]*n
        def find(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1==p2:
                return 0
            
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        
        res=n
        for n1,n2 in edges:
            res-=union(n1,n2)
        return res
        
        
#         uf=Union_find(n)
#         final=[]
#         edges.sort(key=lambda i:i[0])
#         #print(edges)
#         for node1,node2 in edges:
#             final=uf.union(node1,node2)
        
#         visited=set()
#         for ele in final:
#             visited.add(final[ele])
            
#         return len(visited)
#         #print(final)
            
        

# class Union_find:
#     def __init__(self,n):
#         self.parent={i:i for i in range(n)}
        
    
#     def find(self,node):
#         if node==self.parent[node]:
#             return node
#         return self.find(self.parent[node])
    
#     def union(self,node1,node2):
#         root1=self.find(node1)
#         root2=self.find(node2)
#         #print("node1,node2",node1,node2)
#         #print("root1,root2",root1,root2)
#         self.parent[root2]=root1
        
#         return self.parent
    
    
        
        
        
        