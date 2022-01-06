
# // Time Complexity :O(2^(m+n))
# // Space Complexity :O(h), where h is the height of the recursive stack,In the worst case, O(h) = O(mn)
class Solution:
    def __init__(self):
        self.dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        self.maxlen=-inf
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                # print(i,j)
                self.helper(matrix,i,j,1)
                # print(self.maxlen)
        return self.maxlen
    def helper(self,matrix,x,y,length):
        #base
        
        #logic
        self.maxlen=max(self.maxlen,length)
        for i in self.dirs:
            # print(x,y,matrix,i)
            tx=x+i[0]
            ty=y+i[1]
            if (tx>=0 and ty>=0 and tx<=len(matrix)-1 and ty<=len(matrix[0])-1)and abs(matrix[tx][ty])>abs(matrix[x][y]):
                
                
                
                matrix[tx][ty]=-1*matrix[tx][ty]
                # print(matrix,tx,ty,length)
                self.helper(matrix,tx,ty,length+1)
                matrix[tx][ty]=-1*matrix[tx][ty]
                