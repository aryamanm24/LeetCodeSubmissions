# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at mid: split and reverse links of the second half
        prev = None
        curr = slow.next
        slow.next = None

        while(curr is not None):
            ptr = curr.next
            curr.next = prev
            prev = curr
            curr = ptr
        
        # now prev points to the head of the reversed list (last element)
        first = head
        second = prev

        while(second is not None):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        