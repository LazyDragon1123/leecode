# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
        
def merge(root1, root2, tree):
    if root1 is None and root2 is None:
        return
    if root1 is None:
        tree.val = root2.val
        if root2.left is not None:
            tree.left = TreeNode()
            merge(None, root2.left, tree.left)
        if root2.right is not None:
            tree.right = TreeNode()
            merge(None, root2.right, tree.right)
    elif root2 is None:
        tree.val = root1.val
        if root1.left is not None:
            tree.left = TreeNode()
            merge(root1.left, None, tree.left)
        if root1.right is not None:
            tree.right = TreeNode()
            merge(root1.right, None, tree.right)
    else:
        tree.val = root1.val + root2.val
        if root1.left is not None or root2.left is not None:
            tree.left = TreeNode()
            merge(root1.left, root2.left, tree.left)
        if root1.right is not None or root2.right is not None:
            tree.right = TreeNode()
            merge(root1.right, root2.right, tree.right)
    
    
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        tree = TreeNode()
        merge(root1, root2, tree)
        
        return tree
