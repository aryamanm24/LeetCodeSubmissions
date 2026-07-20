# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not list1):
            return list2
        if(not list2):
            return list1
        
        curr1 = list1
        curr2 = list2

        dummy = ListNode(0)
        merged_ptr = dummy

        while(curr1 and curr2):
            if(curr1.val <= curr2.val):
                merged_ptr.next = ListNode(curr1.val)
                merged_ptr = merged_ptr.next
                curr1 = curr1.next
            else:
                merged_ptr.next = ListNode(curr2.val)
                merged_ptr = merged_ptr.next
                curr2 = curr2.next
        
        # reached end of first list
        if(curr1 is None):
            while(curr2):
                merged_ptr.next = ListNode(curr2.val)
                merged_ptr = merged_ptr.next
                curr2 = curr2.next
        else:
            while(curr1):
                merged_ptr.next = ListNode(curr1.val)
                merged_ptr = merged_ptr.next
                curr1 = curr1.next

        return dummy.next
                
