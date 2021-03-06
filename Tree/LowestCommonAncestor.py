# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        #print("root",root.val)
        if (root.val>=q.val and root.val<=p.val) or (root.val>=p.val and root.val<=q.val):
            return root
        
        elif root.val>q.val and root.val>p.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        else:
            return self.lowestCommonAncestor(root.right,p,q)
            
        