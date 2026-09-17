# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftheight=self.heightOfBinaryTree(root.left)
        rightheight=self.heightOfBinaryTree(root.right)
        diameter=leftheight+rightheight
        return max(diameter, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        
    def heightOfBinaryTree(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+ max(self.heightOfBinaryTree(root.left),self.heightOfBinaryTree(root.right))

