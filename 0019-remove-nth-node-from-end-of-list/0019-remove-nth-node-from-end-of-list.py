# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Naive

        curr = head
        length = 0

        while(curr is not None):
            length += 1
            curr = curr.next
        
        # Now we got the length of the linked list, so next we just go till
        # length - n nodes and remove the length - n + 1st node:

        if(n==length):
            return head.next # head is removed

        curr = head
        count = 0

        while(count < length-n-1):
            curr = curr.next
            count += 1
        
        curr.next = curr.next.next
        return head
        
