# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(res, tree, depth):
    if (tree.left is None) and (tree.right is None):
        res.append(depth)
        
    if tree.left not None:
        search(res, tree.left, depth+1)
    
    if tree.right not None:
        search(res, tree.rigjt, depth+1)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = []
        cur = tree
        search(res, cur, 0)
        return min(res)
