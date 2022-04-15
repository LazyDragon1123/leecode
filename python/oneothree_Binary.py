# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(head, level, res):
    if head is None:
        return
    if res.get(level) is None:
        res[level] = [head.val]
    else:
        res[level].append(head.val)
    search(head.left, level + 1, res)
    search(head.right, level + 1, res)


        

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = {}
        search(root, 0, res)
        ans = []
        for key, val in res.items():
            if key % 2 == 0:
                ans.append(val)
            else:
                ans.append(val[::-1])
        return ans
