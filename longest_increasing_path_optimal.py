
# // Time Complexity :o(m*n), worst case 2*o(m*n) as iiterate through all elements twice
# // Space Complexity :O(m*n) size of cache
class Solution:
    def __init__(self):
        self.dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        
        longestpath=-inf
        cache=[[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                # print(i,j)
                longest=self.helper(matrix,cache,m,n,i,j)
                longestpath=max(longestpath,longest)
        return longestpath
            
    def helper(self,matrix,cache,m,n,i,j):
        #base
        if cache[i][j]!=0:
            return cache[i][j]# memoization
        #logic
        ma=0
        for k in self.dirs:
           
            tx=k[0]+i
            ty=k[1]+j
            
            if tx>=0 and ty>=0 and tx<m and ty<n and matrix[tx][ty]>matrix[i][j]:
                
                longest=self.helper(matrix,cache,m,n,tx,ty)
                ma=max(ma,longest)
        cache[i][j]=ma+1
        
        return cache[i][j]