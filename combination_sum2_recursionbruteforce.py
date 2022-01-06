# // Time Complexity :O(2^n),but sorting extra at each step
# // Space Complexity :O(h), where h is the height of the recursive stack
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        if candidates is None:
            return result
        self.helper(candidates, 0, target, [])
        return self.result
    def helper(self, candidates, index, target, path):
        ##base case
        if target==0:
            path.sort()
            print(path,self.result)
            if path not in self.result:
                self.result.append(path)
                return
        if target<0 or index>=len(candidates):
            return
        ##logic
        # print(index)
        
        ##not chose
        # print(path)
        self.helper(candidates, index+1, target, list(path))
        
        
        ##chose
        path.append(candidates[index])
        # print(path)
        self.helper(candidates, index+1, target-candidates[index], list(path))
            