# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Trivial and terminating base cases
        if(not p and not q):
            return True
        
        if(not p or not q):
            return False
        
        if(p.val != q.val):
            return False
        
        left_comparison = self.isSameTree(p.left, q.left)
        right_comparison = self.isSameTree(p.right, q.right)

        return left_comparison and right_comparison
