class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        out=[]
        def dfs(root,max):
            if root is None:
                return 

            if root.val >=max:
                out.append(root.val)
                dfs(root.left,root.val)
                dfs(root.right,root.val)
            else:
                dfs(root.left,max)
                dfs(root.right,max)

            return


        dfs(root,root.val)
        return len(out)