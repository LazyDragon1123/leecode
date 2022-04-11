# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def leveling(head, level, res):
    if not head:
        return
    if res.get(level) is None:
        res[level] = [head.val]
    else:
        res[level].append(head.val)

    leveling(head.left,  level+1, res)
    leveling(head.right,  level+1, res)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        leveling(root, 0, res)
        ret = []
        for val in res.values():
            ret.append(val)
        return ret
