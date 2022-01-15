# // Time Complexity :O(n*k*k)
# // Space Complexity :O(1)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(1,len(costs)):
            for j in range(len(costs[0])):
                
                if j==0:
                    
                    costs[i][j]+=min(costs[i-1][1:])
                elif j==len(costs[0])-1:
                    
                    costs[i][j]+=min(costs[i-1][:j])
                else:
                    costs[i][j]+=min(min(costs[i-1][0:j]),min(costs[i-1][j+1:]))
        return min(costs[-1])
        
