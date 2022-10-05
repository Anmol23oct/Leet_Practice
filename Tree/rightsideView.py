class Solution(object):
    def rightSideView(self, root):

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out=[]
        def rec(node,level):
            if node:
                if len(out)>level:
                    out[level]=node.val
                else:
                    out.append(node.val)
                
                rec(node.left,level+1)
                rec(node.right,level+1)
        rec(root,0)
        return out