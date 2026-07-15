# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # if no linked list, then no cycle
        if (not head):
            return False

        slow_ptr = head
        fast_ptr = head

        while(fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if(slow_ptr == fast_ptr):
                return True
            
        return False