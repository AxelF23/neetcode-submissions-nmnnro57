# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        count = 0
        max_count = float('-inf')
        def dfs(node, count):
            if node is None:
                return count
            left_depth = dfs(node.left, count + 1)
            right_depth = dfs(node.right, count + 1)
            return max(left_depth, right_depth)
        return dfs(node, 0)