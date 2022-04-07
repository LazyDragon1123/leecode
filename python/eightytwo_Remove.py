# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        del_list = []
        while cur:
            if (cur.next is not None) and (cur.next.val == cur.val):
                del_list.append(cur.val)
                cur.next = cur.next.next
            else:
                cur = cur.next
        cur = head
        print(head)
        print(del_list)
        while cur:
            if (cur.next is not None) and (cur.next.val in del_list):
                cur.next = cur.next.next
            else:
                cur = cur.next
        print(head)
        print(head.val)
        print(del_list)
        if head.val in del_list:
            head = head.next
        return head
