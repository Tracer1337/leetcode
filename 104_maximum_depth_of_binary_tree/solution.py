# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root)
    
def depth(root, c = 0):
    if root is None: return c
    return max(depth(root.left, c+1), depth(root.right, c+1))
