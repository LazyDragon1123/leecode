# Definition for a binary tree node.
from selectors import EpollSelector


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def search(head, res, parentval):
#     if (head.left is None) and (head.right is None):
#         return
#     elif (head.left is not None) and (head.right is not None):
#         if (head.left.val < head.val) and (head.right.val > head.val) and (((parentval < head.val) and (parentval < head.right.val)) or ((parentval > head.val) and (parentval > head.left.val))):
#             search(head.left, res, head.val)
#             search(head.right, res, head.val)
#         else:
#             res.append(True)
#             return
#     elif (head.left is None) and (head.right is not None):
#         if (head.right.val > head.val) and (((parentval < head.val) and (parentval < head.right.val)) or (parentval > head.val)):
#             search(head.right, res, head.val)
#         else:
#             res.append(True)
#             return
#     else:
#         if (head.left.val < head.val) and (((parentval < head.val)) or ((parentval > head.val) and (parentval > head.left.val))):
#             search(head.left, res, head.val)
#         else:
#             res.append(True)
#             return
    
def search(head, right, left):
    if head is None:
        return True
    if not((right > head.val) and (left < head.val)):
        return False
    return (search(head.left, head.val, left) and search(head.right, right, head.val))
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return search(root, float('inf'), float('-inf'))

        