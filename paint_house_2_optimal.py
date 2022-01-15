# // Time Complexity :O(n*k)
# // Space Complexity :O(1)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        pre_min_1=inf
        pre_min_2=inf
        pre_min_1_idx=None
        pre_min_2_idx=None
        for j in range(len(costs[0])):
                
                if pre_min_1 > costs[0][j]:
                    pre_min_2=pre_min_1
                    pre_min_1=costs[0][j]
                    pre_min_2_idx=pre_min_1_idx
                    pre_min_1_idx=j
                elif pre_min_2>costs[0][j]:
                    pre_min_2=costs[0][j]
                    pre_min_2_idx=j
        
        
                
            
            
        for i in range(1,len(costs)):
            
            print(pre_min_1,pre_min_2,pre_min_1_idx,pre_min_2_idx)
                
            for j in range(len(costs[0])):
                if j==pre_min_1_idx:
                    costs[i][j]+=costs[i-1][pre_min_2_idx]
                else:
                    costs[i][j]+=costs[i-1][pre_min_1_idx]
            pre_min_1=inf
            pre_min_2=inf
            pre_min_1_idx=None
            pre_min_2_idx=None
            for j in range(len(costs[0])):
                
                if pre_min_1 > costs[i][j]:
                    pre_min_2=pre_min_1
                    pre_min_1=costs[i][j]
                    pre_min_2_idx=pre_min_1_idx
                    pre_min_1_idx=j
                elif pre_min_2>costs[i][j]:
                    pre_min_2=costs[i][j]
                    pre_min_2_idx=j
            
                    
#             pre_min_1=min_1
#             pre_min_1_idx=min_1_idx
#             pre_min_2=min_2
#             pre_min_2_idx=min_2_idx
            print(costs)
            
                
        return min(costs[-1])
        