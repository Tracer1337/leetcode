# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        if abs(size(root.left) - size(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
def size(root, s = 0):
    if root is None: return s
    return max(size(root.left, s+1), size(root.right, s+1))
