# // Time Complexity :O(n), go through all nodes
# // Space Complexity :O(h), where h is the height of the recursive stack-av case h=logn, balanced binary tree but worst case h=n skewed tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodeval=-inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.nodeval
    def helper(self,node):
        #base
        if not node:
            return 0
        #logic
        #left branch
        case1=max(self.helper(node.left),0)
        #right branck
        case2=max(self.helper(node.right),0)
        print(case1,case2,node.val)
        self.nodeval=max(self.nodeval,case1+case2+node.val)
        print(self.nodeval)
        return node.val+max(case1,case2)
        