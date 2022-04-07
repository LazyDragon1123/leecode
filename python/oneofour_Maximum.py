# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def search(tree, maxdepth, cands):
    if (tree.left is None) and (tree.right is None):
        return cands.append(maxdepth)
    if tree.left is not None:
        search(tree.left, maxdepth+1, cands)
    if tree.right is not None:
        search(tree.right, maxdepth+1, cands)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        cands = []
        search(root, 0, cands)
        return max(cands)+1
        