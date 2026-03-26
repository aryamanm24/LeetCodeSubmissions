# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if(not root):
            return None
        
        left_subtree = self.invertTree(root.left)
        right_subtree = self.invertTree(root.right)

        # now that I have the left and right subtree of this
        # return call, I connect the root's left to right_tree
        # and root's right to left_tree

        root.left = right_subtree
        root.right = left_subtree
        return root