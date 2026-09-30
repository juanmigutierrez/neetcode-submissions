# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: #Not NULL
            next_node = curr.next # save the next next node in temporal

            curr.next = prev #reverse the pointer curr <- prev
            prev = curr
            curr = next_node

        return prev
