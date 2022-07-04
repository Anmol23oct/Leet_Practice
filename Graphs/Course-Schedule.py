class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        maps={i:[] for i in range(numCourses)}
        for ele in prerequisites:
            
            one=ele[0]
            two=ele[1]
            maps[one].append(two)
        print(maps)
        visitSet=set()
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if maps[crs]==[]:
                return True
            
            visitSet.add(crs)
            
            for m in maps[crs]:
                if not dfs(m): return False
            
            visitSet.remove(crs)
            maps[crs]=[]
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True
#         maps={i:[] for i in range(numCourses)}
#         #print(maps)
#         for ele in prerequisites:
#             one=ele[0]
#             two=ele[1]
#             maps[one].append(two)
        
#         print(maps)
#         visited=set()
#         for ele in maps:
#             visited.add(ele)
#             for i in range(maps[ele]):
#                 dfs(i,visited)
        
#         def dfs(i,visited):
            
        
        
            
            
            
        