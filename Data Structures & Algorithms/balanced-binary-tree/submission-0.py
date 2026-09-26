# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return True, 0
            
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)
            print(root.val, leftBalanced and rightBalanced, max(leftHeight, rightHeight) + 1)
            return leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
        
        balanced, height = dfs(root)
        return balanced
