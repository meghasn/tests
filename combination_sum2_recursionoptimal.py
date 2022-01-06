# // Time Complexity :O(2^n)
# // Space Complexity :O(h), where h is the height of the recursive stack
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        if candidates is None:
            return result
        candidates.sort()
        self.helper(candidates, 0, target, [],1)
        return self.result
    def helper(self, candidates, index, target, path,flag):
        ##base case
        if flag==0 and index<len(candidates):
            print(index)
            while index<len(candidates) and candidates[index]==candidates[index-1]:
                index+=1
                print("x",index)
                
        if target==0:
            
            
            if path not in self.result:
                self.result.append(path)
                return
        if target<0 or index>=len(candidates):
            return
        ##logic
        # print(index)
        prev=-1
        
        ##not chose
        self.helper(candidates, index+1, target, list(path),0)
        print("c",candidates[index])
        
        ##chose
        # while candidates[index]!=candidates[index+1]:
        #     index+=1
        path.append(candidates[index])
        print(path)
        self.helper(candidates, index+1, target-candidates[index], list(path),1)
        print("x")
        path.pop()
            