# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.left is None and root.right is None: return True
        if root.left is None or root.right is None: return False
        return self.isSymmetricRecursive(root.left, root.right)
    
    def isSymmetricRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False
        return self.isSymmetricRecursive(p.left, q.right) and self.isSymmetricRecursive(p.right, q.left)
