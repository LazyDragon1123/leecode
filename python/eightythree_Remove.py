class ListNode: 
    def __init__(self, x): 
        self.val = x 
        self.next = None

class Solution: 
    def deleteDuplicates(self, head:ListNode):
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
