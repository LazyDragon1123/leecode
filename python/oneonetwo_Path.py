# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sumsearch(res, node, sum):
    if not node:
        return
    if (node.left is None) and (node.right is None):
        res.append(sum + node.val)
        return
    
    if node.left:
        sumsearch(res, node.left, sum+node.val)
    
    if node.right:
        sumsearch(res, node.right, sum+node.val)
    
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        sumsearch(res, root, 0)
        if (root) and ((root.left is None) and (root.right is None)):
            res = [root.val]
        return targetSum in res
