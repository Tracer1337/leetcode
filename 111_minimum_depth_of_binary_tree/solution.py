# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        nodes, i = [root], 1
        while len(nodes) > 0:
            newNodes = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return i
                if node.left is not None:
                    newNodes.append(node.left)
                if node.right is not None:
                    newNodes.append(node.right)
            nodes = newNodes
            i += 1
