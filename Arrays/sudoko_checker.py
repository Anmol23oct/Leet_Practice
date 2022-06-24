class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d={}
        for i in range(9):
            for j in range(9):
                if (i,j) not in d:
                    
                    if board[i][j]=='.':
                        
                        d[i,j]=0
                    
                    else:
                        d[i,j]=int(board[i][j])
        
        #print(d)
        #row
        for i in range(9):
            dup={}
            for j in range(9):
                dup[d[i,j]]=dup.get(d[i,j],0)+1
            
            for ele in dup:
                if ele!=0 and dup[ele]>1:
                    return False
        
        #col
        for i in range(9):
            dup={}
            for j in range(9):
                dup[d[j,i]]=dup.get(d[j,i],0)+1
            
            
            for ele in dup:
                if ele!=0 and dup[ele]>1:
                    return False
        
        #3x3
        i=0
        j=0
        while i<9:
            dup={}
            for k in range(i,i+3):
                for l in range(j,j+3):
                    dup[d[k,l]]=dup.get(d[k,l],0)+1
                    
            for ele in dup:
                if ele!=0 and dup[ele]>1:
                    return False
            print("dup",dup)
            j=j+3
            if j==9:
                j=0
                i=i+3
            print("j=",j)
        
        return True
            
            
        