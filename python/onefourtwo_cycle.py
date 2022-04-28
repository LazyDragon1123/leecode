# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = head
#         slow = head
#         while(fast.next.next is not None):
#             fast = fast.next.next
#             slow = slow.next
#             if fast.val == slow.val:
#                 return slow
            
#         return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = fast = head
        cout = 0
        flag = False
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            cout += 1
            if slow == fast:
                flag = True
                break
        if flag == False:
            return None
        slow = head
        while(slow.next is not None):
            tmp = slow
            c = 0
            while (c != cout):
                tmp = tmp.next
                c += 1
            if tmp == slow:
                return slow
            slow = slow.next
            
        return None
