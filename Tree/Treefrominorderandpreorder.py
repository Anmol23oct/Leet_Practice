# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        
        if len(preorder)==0:
            return None
        r=preorder[0]
        root=TreeNode(r)
        newInorderLeft,newInorderRight,newPreorderLeft,newPreorderRight = self.GetCorrectOrder(r,preorder,inorder)
        leftSubTree=self.buildTree(newPreorderLeft,newInorderLeft)
        rightSubTree=self.buildTree(newPreorderRight,newInorderRight)
        root.left=leftSubTree
        root.right=rightSubTree
        
        return root
        
        
        
        
        
        
    def GetCorrectOrder(self,root,preorder,inorder):
        
        newil=[]
        newir=[]
        i=0
        #print("root",root)
        #print("inorder=",inorder)
        for ele in inorder:
            if ele==root:
                break
            newil.append(inorder[i])
            i=i+1
        #print("newil",newil)
        j=1
        newpl=[]
        newpr=[]
        for t in range(1,i+1):
        #while(j<=i):
            newpl.append(preorder[t])
            j=j+1
        #print("newpl",newpl)
        
        i=i+1
        for g in range(i,len(inorder)):
        #while(i<len(inorder)):
            newir.append(inorder[g])
            i=i+1
        #print("newir",newir)
        
        for s in range(j,len(preorder)):
        #while(j<len(preorder)):
            newpr.append(preorder[s])
            j=j+1
        #print("newpr",newpr)
        
        return newil,newir,newpl,newpr
        