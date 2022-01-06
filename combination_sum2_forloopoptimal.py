# // Time Complexity :O(2^n)
# // Space Complexity :O(h), where h is the height of the recursive stack
import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        if candidates is None:
            return result
        candidates.sort()
        self.helper(candidates, 0, target, [])
        return self.result
    def helper(self, candidates, index, target, path):
        ##base case
        if target==0:
            print(path)
            self.result.append(copy.copy(path))
            return
        if target<0:
            return
        ##logic
        prev=-1
        for i in range(index,len(candidates)):
            if candidates[i]==prev:
                continue
            path.append(candidates[i])
            print(path)
            self.helper(candidates,i+1,target-candidates[i],path)
            path.pop()
            prev=candidates[i]
            