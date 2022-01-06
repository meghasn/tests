# // Time Complexity :O(2^n),but sorting extra at each step
# // Space Complexity :O(h), where h is the height of the recursive stack
import copy
class Solution:
    def __init__(self):
        self.res=[]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.helper([],candidates,target,0)
        return self.res
    def helper(self,path,candidates,s,index):
        #base
        
        if s<0 or index>len(candidates):
            return
        elif s==0:
            li=copy.copy(path)
            li.sort()
            if li not in self.res:
                self.res.append(li)
            
            
        #logic
        for i in range(index,len(candidates)):
            
    
            path.append(candidates[i])
            
            self.helper(path,candidates,s-candidates[i],i+1)
            path.pop()