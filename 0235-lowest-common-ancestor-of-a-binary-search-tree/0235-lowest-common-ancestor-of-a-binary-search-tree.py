# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Idea: At any node, if p and q are both less than node,
        # then, LCA in left_subtree. If both greater than node, then
        # LCA in right_subtree. If branch, one in left and one in right
        # then, node is LCA.

        curr = root

        while (curr is not None):

            if(p.val < curr.val and q.val < curr.val):
                curr = curr.left
            elif(p.val > curr.val and q.val > curr.val):
                curr = curr.right
            else:
                return curr
        