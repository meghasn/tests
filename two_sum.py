#time m+n,space h
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag=False
        self.hset=set()
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.helper(root1,1,target)
        self.helper(root2,2,target)
        return self.flag
    def helper(self,root,treeno,target):
        #base
        if root is None:
            return
        #logic
        self.helper(root.left,treeno,target)
        if treeno==1:
            if target-root.val not in self.hset:
                self.hset.add(target-root.val)
                
        if treeno==2:
            if root.val in self.hset:
                self.flag=True
            
        
                
        self.helper(root.right,treeno,target)