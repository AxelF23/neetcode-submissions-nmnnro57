# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        curr = new_head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        new_head = prev
        p1 = head
        p2 = new_head
        while p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next

