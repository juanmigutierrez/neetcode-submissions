# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Separate in two list 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'slow' is the last node of the first half.
        #
        # Example:
        # 1 → 2 → 3 → 4 → 5
        #         ↑
        #        slow
        #
        # First half:  1 → 2 → 3
        # Second half: 4 → 5

        second = slow.next

        #disconnect first halfo from the second half
        prev = slow.next = None

        #Reverse second half
        while second:
            tmp = second.next #Save the next node before changing the pointer
            second.next = prev # reverse current node pointer
            prev = second #move prev forward
            second = tmp #move second forward


        # At this point:
        #
        # First half:   1 → 2 → 3
        # Second half:  5 → 4
        #
        # 'prev' is now the head of the reversed second half.


        #Merge two halvees
        first, second = head,prev

        while second:
            tmp1, tmp2 = first.next,second.next #save next nodes, because we will overwrite them
            first.next = second 
            second.next = tmp1

            first, second = tmp1, tmp2





        
            