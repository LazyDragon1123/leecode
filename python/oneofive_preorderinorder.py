# Definition for a binary tree node.
from distutils.command.build import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        nodeind = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:nodeind+1], inorder[:nodeind ])
        root.right = self.buildTree(preorder[nodeind+1:], inorder[nodeind + 1 :])
        
        return root
        
        