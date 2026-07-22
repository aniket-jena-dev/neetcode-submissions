# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            lmx = dfs(root.left)
            rmx = dfs(root.right)
            lmx = max(lmx, 0)
            rmx = max(rmx, 0)

            res[0] = max(res[0], root.val + lmx + rmx)

            return max(root.val, root.val + max(lmx, rmx))
        
        dfs(root)
        
        return res[0]

        