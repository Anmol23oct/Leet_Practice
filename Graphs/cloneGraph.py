"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        maps={}
        
        def clone(node):
            if node in maps:
                return maps[node]
            
            copy=Node(node.val)
            maps[node]=copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
                
            return copy
        
        if node:
            return clone(node)
        else:
            return None
                
        
