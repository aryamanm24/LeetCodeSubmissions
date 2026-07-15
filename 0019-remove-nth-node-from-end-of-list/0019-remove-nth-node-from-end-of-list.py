# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if(not head):
            return head
        
        length = 0
        curr = head

        while(curr):
            length += 1
            curr = curr.next

        # Now we know the number of nodes in the linked list
        i = 1
        curr = head

        number_to_remove = length - n + 1

        # removing the head
        if(number_to_remove == 1):
            return head.next

        while(i < number_to_remove):
            prev = curr
            curr = curr.next
            i += 1
        
        if(prev.next is None):
            return head
        
        prev.next = curr.next
        return head